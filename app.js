// KPSS 2026 Uygulama Mantığı (app.js)

let currentSubjectId = "matematik";
let currentTopicId = "mat_1";
let currentDifficultyFilter = "tumu";
let currentTextbookPageIndex = 0;
let userAnswers = JSON.parse(localStorage.getItem("kpss_user_answers") || "{}");
let checkedPlanTasks = JSON.parse(localStorage.getItem("kpss_plan_tasks") || "{}");

// Deneme Sınavı Durum Değişkenleri
let currentMockIndex = 0;
let mockUserAnswers = {};
let isMockStarted = false;
let isMockPaused = false;
let isMockSubmitted = false;
let mockTimerInterval = null;
let mockTimeRemaining = 130 * 60; // 130 Dakika saniye cinsinden

// --- PROFESYONEL EKLENTİ: DENEME DURUMUNU OTOMATİK KAYDETME ---
function saveMockState() {
  const state = {
    examId: currentMockExamId,
    answers: mockUserAnswers,
    timeRemaining: mockTimeRemaining,
    isStarted: isMockStarted,
    isSubmitted: isMockSubmitted
  };
  localStorage.setItem("kpss_mock_state_" + currentMockExamId, JSON.stringify(state));
}

function loadMockState(examId) {
  const saved = localStorage.getItem("kpss_mock_state_" + examId);
  if (saved) {
    const state = JSON.parse(saved);
    mockUserAnswers = state.answers || {};
    mockTimeRemaining = state.timeRemaining || (130 * 60);
    isMockStarted = state.isStarted || false;
    isMockSubmitted = state.isSubmitted || false;
  } else {
    mockUserAnswers = {};
    localStorage.removeItem("kpss_mock_state_" + examId);
    mockTimeRemaining = 130 * 60;
    isMockStarted = false;
    isMockSubmitted = false;
    isMockPaused = false;
  }
}


document.addEventListener("DOMContentLoaded", () => {
  initCountdown();
  initTheme();
  initNavigation();
  renderDashboardSubjects();
  renderStudyPlan();
  renderSubjectFilterTabs();
  renderTopicQuestions();
  initMockExam();
  updateGlobalStats();
});

/* 1. Geri Sayım Canlı Sayacı (25 Ekim 2026) */
function initCountdown() {
  const targetDate = new Date(KPSS_DATA.examDate).getTime();

  function update() {
    const now = new Date().getTime();
    const diff = targetDate - now;

    if (diff <= 0) {
      document.getElementById("cnt-days").innerText = "00";
      document.getElementById("cnt-hours").innerText = "00";
      document.getElementById("cnt-mins").innerText = "00";
      document.getElementById("cnt-secs").innerText = "00";
      return;
    }

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const secs = Math.floor((diff % (1000 * 60)) / 1000);

    document.getElementById("cnt-days").innerText = String(days).padStart(2, "0");
    document.getElementById("cnt-hours").innerText = String(hours).padStart(2, "0");
    document.getElementById("cnt-mins").innerText = String(mins).padStart(2, "0");
    document.getElementById("cnt-secs").innerText = String(secs).padStart(2, "0");
  }

  update();
  setInterval(update, 1000);
}

/* 2. Tema Geçişi (Karanlık / Aydınlık) */
function initTheme() {
  const savedTheme = localStorage.getItem("kpss_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  document.getElementById("theme-icon").innerText = savedTheme === "dark" ? "🌙" : "☀️";

  document.getElementById("theme-toggle").addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");
    const next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("kpss_theme", next);
    document.getElementById("theme-icon").innerText = next === "dark" ? "🌙" : "☀️";
  });
}

/* 3. Tab Navigasyonu */
function initNavigation() {
  const navItems = document.querySelectorAll(".nav-item");
  navItems.forEach((item) => {
    item.addEventListener("click", () => {
      const tabId = item.getAttribute("data-tab");
      switchTab(tabId);
    });
  });
}

function switchTab(tabId) {
  document.querySelectorAll(".nav-item").forEach((el) => el.classList.remove("active"));
  document.querySelectorAll(".tab-pane").forEach((el) => el.classList.remove("active"));

  const targetNav = document.querySelector(`.nav-item[data-tab="${tabId}"]`);
  const targetPane = document.getElementById(`pane-${tabId}`);

  if (targetNav) targetNav.classList.add("active");
  if (targetPane) targetPane.classList.add("active");

  window.scrollTo({ top: 0, behavior: "smooth" });
}

/* 4. Dashboard Ders Kartları */
function renderDashboardSubjects() {
  const container = document.getElementById("dashboard-subjects-grid");
  if (!container) return;

  container.innerHTML = KPSS_DATA.subjects
    .map(
      (sub) => `
    <div class="subject-card" onclick="selectSubjectFromDashboard('${sub.id}')">
      <div class="subject-icon">${sub.icon}</div>
      <div class="subject-name">${sub.name}</div>
      <div class="subject-desc">${sub.description}</div>
      <div class="subject-meta">
        <span>${sub.topics.length} Ana Konu</span>
        <span>${sub.questionCount} Soru Dağılımı</span>
      </div>
    </div>
  `
    )
    .join("");
}

function selectSubjectFromDashboard(subId) {
  currentSubjectId = subId;
  const sub = KPSS_DATA.subjects.find((s) => s.id === subId);
  if (sub && sub.topics.length > 0) {
    currentTopicId = sub.topics[0].id;
  }
  renderSubjectFilterTabs();
  renderTopicQuestions();
  switchTab("subjects-lessons");
}

/* 5. 12 Haftalık Çalışma Programı */
function renderStudyPlan() {
  const container = document.getElementById("plan-timeline-container");
  if (!container) return;

  container.innerHTML = KPSS_DATA.studyPlan
    .map(
      (plan) => `
    <div class="week-card">
      <div class="week-header">
        <div class="week-title">${plan.title}</div>
        <div class="week-badge">⏱️ ${plan.hoursPerDay}</div>
      </div>
      <div class="week-focus">🎯 <b>Odak:</b> ${plan.focus}</div>
      <ul class="task-list">
        ${plan.tasks
          .map((task, idx) => {
            const taskId = `w${plan.week}_t${idx}`;
            const isChecked = checkedPlanTasks[taskId] ? "checked" : "";
            return `
            <li class="task-item">
              <input type="checkbox" class="task-checkbox" id="${taskId}" ${isChecked} onchange="togglePlanTask('${taskId}')">
              <label for="${taskId}">${task}</label>
            </li>
          `;
          })
          .join("")}
      </ul>
    </div>
  `
    )
    .join("");
}

function togglePlanTask(taskId) {
  checkedPlanTasks[taskId] = !checkedPlanTasks[taskId];
  localStorage.setItem("kpss_plan_tasks", JSON.stringify(checkedPlanTasks));
  updateGlobalStats();
}

/* 6. Ders ve Konu Filtreleme (Sade Dropdown & Butonlar) */
function renderSubjectFilterTabs() {
  const subContainer = document.getElementById("subject-filter-tabs");
  if (!subContainer) return;

  subContainer.innerHTML = KPSS_DATA.subjects
    .map(
      (s) => `
    <button class="topic-tab-btn ${s.id === currentSubjectId ? "active" : ""}" onclick="changeSubject('${s.id}')">
      ${s.icon} ${s.name}
    </button>
  `
    )
    .join("");

  renderTopicFilterTabs();
}

function renderTopicFilterTabs() {
  const topContainer = document.getElementById("topic-filter-tabs");
  if (!topContainer) return;

  const currentSub = KPSS_DATA.subjects.find((s) => s.id === currentSubjectId);
  if (!currentSub) return;

  // Dropdown Select for clean UI
  topContainer.innerHTML = `
    <select class="topic-dropdown-select" style="width: 100%; padding: 10px 16px; border-radius: var(--radius-md); background: var(--bg-primary); color: var(--text-primary); border: 1px solid var(--border-color); font-weight: 600; font-size: 0.95rem; cursor: pointer;" onchange="changeTopic(this.value)">
      ${currentSub.topics
        .map(
          (t) => `
        <option value="${t.id}" ${t.id === currentTopicId ? "selected" : ""}>
          📌 ${t.title} (${t.avgQuestions})
        </option>
      `
        )
        .join("")}
    </select>
  `;

  renderTopicSummary();
}

function changeSubject(subId) {
  currentSubjectId = subId;
  currentTextbookPageIndex = 0;
  const sub = KPSS_DATA.subjects.find((s) => s.id === subId);
  if (sub && sub.topics.length > 0) {
    currentTopicId = sub.topics[0].id;
  }
  renderSubjectFilterTabs();
  renderTopicQuestions();
}

function changeTopic(topicId) {
  currentTopicId = topicId;
  currentTextbookPageIndex = 0;
  renderTopicFilterTabs();
  renderTopicQuestions();
}

function filterDifficulty(level) {
  currentDifficultyFilter = level;
  document.querySelectorAll(".level-filter-btn").forEach((btn) => {
    btn.classList.remove("active");
  });
  if (event && event.target) {
    event.target.classList.add("active");
  }
  renderTopicQuestions();
}

/* SAYFA SAYFA DETAYLI DERS KİTABI OKUYUCU MODÜLÜ */
function renderTopicSummary() {
  const summaryBox = document.getElementById("topic-summary-container");
  if (!summaryBox) return;

  const currentSub = KPSS_DATA.subjects.find((s) => s.id === currentSubjectId);
  const currentTopic = currentSub?.topics.find((t) => t.id === currentTopicId);

  if (!currentTopic) {
    summaryBox.style.display = "none";
    return;
  }

  summaryBox.style.display = "block";

  // Sayfa Sayfa Ders Kitabı Okuma Verisi
  const pages = currentTopic.pages || [
    {
      pageNo: "1",
      pageTitle: `Sayfa 1: ${currentTopic.title} Detaylı Ders Anlatımı`,
      text: `
        <h3>📖 ${currentTopic.title} - Tam Detaylı Ders Kitabı Anlatımı</h3>
        <p style="line-height: 1.8; margin: 12px 0;">${currentTopic.summary}</p>
      `
    }
  ];

  const activePage = pages[currentTextbookPageIndex] || pages[0];

  // Remove forced global SVG diagram
  let svgDiagramHTML = "";

  // Worked Examples Section (Örnek Çözümlü Sorular)
  let workedExamplesHTML = "";
  if (currentTopic.questions && currentTopic.questions.length > 0) {
    workedExamplesHTML = `
      <div style="margin-top: 24px; border-top: 1px dashed var(--border-color); padding-top: 20px;">
        <h4 style="font-size: 1.15rem; color: #60a5fa; margin-bottom: 14px;">🧠 Konuyu Anlama Rehberi: Örnek Çözümlü Sorular & İnceleme</h4>
        <div style="display: flex; flex-direction: column; gap: 16px;">
          ${currentTopic.questions
            .map(
              (q, idx) => `
            <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 18px;">
              <div style="font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">
                💡 Örnek Rehber Soru ${idx + 1}: ${q.text}
              </div>
              <div style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 12px;">
                <b>Şıklar:</b> ${q.options.join(" | ")}
              </div>
              <div style="background: rgba(16, 185, 129, 0.08); border-left: 4px solid var(--accent-emerald); padding: 14px; border-radius: 6px; font-size: 0.92rem; color: #a7f3d0; line-height: 1.7;">
                <b>✅ Doğru Cevap:</b> ${q.options[q.correct]}<br>
                <b>📝 Adım Adım Detaylı Konu Anlatımlı Çözüm:</b> ${q.solution}
              </div>
            </div>
          `
            )
            .join("")}
        </div>
      </div>
    `;
  }

  summaryBox.innerHTML = `
    <!-- Top Bar with Chapter Tabs -->
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 14px; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
      <div>
        <h3 style="font-size: 1.4rem; color: #60a5fa;">📖 ${currentTopic.title}</h3>
        <p style="font-size: 0.85rem; color: var(--text-secondary); margin-top: 4px;">Sıfırdan Başlayanlar İçin Detaylı Ders Kitabı Okuma Modülü</p>
      </div>
      <div style="display: flex; gap: 8px;">
        <span style="background: rgba(16, 185, 129, 0.15); color: #34d399; padding: 6px 16px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">
          ⏱️ 3-4 Saatlik Detaylı Okuma
        </span>
      </div>
    </div>

    <!-- Page Selector Toolbar (Clean Stepper Tabs) -->
    <div class="topic-selector-tabs" style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;">
      ${pages
        .map(
          (p, pIdx) => `
        <button class="topic-tab-btn ${pIdx === currentTextbookPageIndex ? "active" : ""}" onclick="switchTextbookPage(${pIdx})">
          📄 ${p.pageTitle}
        </button>
      `
        )
        .join("")}
    </div>

    <!-- Full Reading Content Box -->
    <div style="font-size: 1.05rem; line-height: 1.9; color: var(--text-primary); background: rgba(255,255,255,0.02); padding: 28px; border-radius: var(--radius-lg); border: 1px solid var(--border-color); box-shadow: var(--shadow-lg);">
      <div style="font-weight: 800; font-size: 1.25rem; color: var(--accent-blue); margin-bottom: 18px; border-bottom: 2px solid rgba(59,130,246,0.3); padding-bottom: 8px;">
        ${activePage.pageTitle}
      </div>

      <div>
        ${activePage.text}
      </div>

      ${svgDiagramHTML}

      <!-- Key OSYM Points -->
      ${
        currentTopic.keyPoints && currentTopic.keyPoints.length > 0
          ? `
        <div style="background: rgba(245, 158, 11, 0.08); border-left: 4px solid var(--accent-amber); padding: 16px 20px; border-radius: var(--radius-sm); margin: 24px 0 0 0;">
          <div style="font-weight: 700; color: #fbbf24; font-size: 1rem; margin-bottom: 8px;">⚠️ ÖSYM Sınav Tüyoları & Çıkmış Soru Vurguları:</div>
          <ul class="key-points-list" style="margin-top: 4px; font-size: 0.95rem; line-height: 1.7;">
            ${currentTopic.keyPoints.map((pt) => `<li style="margin-bottom: 8px;">${pt}</li>`).join("")}
          </ul>
        </div>
      `
          : ""
      }
    </div>

    ${workedExamplesHTML}

    <!-- Page Navigation Prev / Next Buttons -->
    <div style="display: flex; justify-content: space-between; margin-top: 24px;">
      <button class="btn-solution" ${currentTextbookPageIndex === 0 ? "disabled style='opacity:0.4;'" : ""} onclick="switchTextbookPage(${currentTextbookPageIndex - 1})">
        ⬅️ Önceki Sayfa
      </button>

      <span style="font-weight: 700; color: var(--text-secondary); font-size: 0.9rem; align-self: center;">
        Sayfa ${currentTextbookPageIndex + 1} / ${pages.length}
      </span>

      <button class="hero-cta" style="padding: 10px 24px; font-size: 0.9rem;" ${currentTextbookPageIndex === pages.length - 1 ? "disabled style='opacity:0.4;'" : ""} onclick="switchTextbookPage(${currentTextbookPageIndex + 1})">
        Sonraki Sayfa ➡️
      </button>
    </div>
  `;
}

function switchTextbookPage(pageIdx) {
  currentTextbookPageIndex = pageIdx;
  renderTopicSummary();
  window.scrollTo({ top: 300, behavior: "smooth" });
}

/* 7. İnteraktif Soru Bankası Render & İşaretleme */
function renderTopicQuestions() {
  const container = document.getElementById("topic-questions-container");
  const countLabel = document.getElementById("topic-question-count-label");
  if (!container) return;

  const currentSub = KPSS_DATA.subjects.find((s) => s.id === currentSubjectId);
  const currentTopic = currentSub?.topics.find((t) => t.id === currentTopicId);

  if (!currentTopic || !currentTopic.questions || currentTopic.questions.length === 0) {
    container.innerHTML = `
      <div style="background: var(--bg-secondary); padding: 32px; border-radius: var(--radius-lg); text-align: center;">
        <p style="color: var(--text-secondary);">Bu konu için hazırlanan örnek sorular yükleniyor...</p>
      </div>
    `;
    if (countLabel) countLabel.innerText = "Gösterilen Soru: 0";
    return;
  }

  let filteredQuestions = currentTopic.questions;
  if (currentDifficultyFilter !== "tumu") {
    filteredQuestions = currentTopic.questions.filter((q) => q.level === currentDifficultyFilter);
  }

  if (countLabel) {
    countLabel.innerText = `Gösterilen Soru: ${filteredQuestions.length} / ${currentTopic.questions.length}`;
  }

  if (filteredQuestions.length === 0) {
    container.innerHTML = `
      <div style="background: var(--bg-secondary); padding: 32px; border-radius: var(--radius-lg); text-align: center;">
        <p style="color: var(--text-secondary);">'${currentDifficultyFilter}' seviyesinde soru bulunamadı.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <h3 style="margin-bottom: 16px; font-size: 1.2rem; color: var(--text-primary);">✍️ Kendini Test Et (İnteraktif Soru Bankası Testi)</h3>
    ${filteredQuestions
      .map((q, qIdx) => {
        const savedChoice = userAnswers[q.id];
        const hasAnswered = savedChoice !== undefined;
        const isCorrectChoice = hasAnswered && savedChoice === q.correct;

        return `
        <div class="question-card" id="card-${q.id}">
          <div class="question-card-header">
            <span style="font-weight: 700; color: var(--accent-blue);">Soru ${qIdx + 1}</span>
            <span class="difficulty-badge ${q.level.toLowerCase()}">${q.level}</span>
          </div>

          <div class="question-text">${q.text}</div>

          <div class="options-grid">
            ${q.options
              .map((opt, optIdx) => {
                let stateClass = "";
                if (hasAnswered) {
                  if (optIdx === q.correct) stateClass = "correct";
                  else if (optIdx === savedChoice) stateClass = "wrong";
                }

                return `
                <div class="option-pill ${stateClass} ${savedChoice === optIdx ? "selected" : ""}" 
                     onclick="selectQuestionOption('${q.id}', ${optIdx}, ${q.correct})">
                  <span>${opt}</span>
                  ${hasAnswered && optIdx === q.correct ? '<span>✅ Doğru</span>' : ''}
                  ${hasAnswered && optIdx === savedChoice && optIdx !== q.correct ? '<span>❌ Yanıtınız</span>' : ''}
                </div>
              `;
              })
              .join("")}
          </div>

          <div class="question-actions">
            <button class="btn-solution" onclick="toggleSolution('${q.id}')">🔍 Çözümü Göster / Gizle</button>
            ${
              hasAnswered
                ? `<span style="font-weight: 700; font-size: 0.9rem; color: ${isCorrectChoice ? "#34d399" : "#f87171"};">
                    ${isCorrectChoice ? "🎉 Tebrikler, Doğru!" : "⚠️ Yanlış Cevap"}
                   </span>`
                : ""
            }
          </div>

          <div class="solution-box" id="sol-${q.id}">
            <b>📝 Detaylı Adım Adım Çözüm:</b><br>
            ${q.solution}
          </div>
        </div>
      `;
      })
      .join("")}
  `;
}

function selectQuestionOption(qId, selectedIdx, correctIdx) {
  userAnswers[qId] = selectedIdx;
  localStorage.setItem("kpss_user_answers", JSON.stringify(userAnswers));
  renderTopicQuestions();
  updateGlobalStats();
}

function toggleSolution(qId) {
  const solBox = document.getElementById(`sol-${qId}`);
  if (solBox) {
    solBox.classList.toggle("visible");
  }
}

/* 8. 120 Soruluk Deneme Sınavı Motoru, 10 Farklı Deneme Desteği & İnceleme Modu */
let currentMockExamId = "deneme_1";

function getActiveMockExam() {
  if (KPSS_DATA.mockExams && KPSS_DATA.mockExams.length > 0) {
    const found = KPSS_DATA.mockExams.find((e) => e.id === currentMockExamId);
    return found || KPSS_DATA.mockExams[0];
  }
  return KPSS_DATA.mockExam;
}

function populateMockExamCards() {
  const container = document.getElementById("deneme-cards-container");
  const badgeEl = document.getElementById("active-deneme-badge");
  if (!container) return;

  const exams = KPSS_DATA.mockExams || [KPSS_DATA.mockExam];
  
  // Aktif deneme rozetini güncelle
  const currentIdx = exams.findIndex((e) => (e.id || "") === currentMockExamId);
  const examNumber = currentIdx >= 0 ? currentIdx + 1 : 1;
  if (badgeEl) {
    badgeEl.innerText = `${examNumber}. Deneme Aktif`;
  }

  container.innerHTML = exams
    .map((exam, idx) => {
      const examId = exam.id || `deneme_${idx + 1}`;
      const isActive = examId === currentMockExamId;
      return `
        <button class="deneme-card-btn ${isActive ? "active" : ""}" onclick="changeMockExam('${examId}')">
          <span>${idx + 1}. Deneme</span>
          <span class="sub-tag">${isActive ? "● Aktif" : "120 Soru"}</span>
        </button>
      `;
    })
    .join("");
}

function changeMockExam(examId) {
  if (examId === currentMockExamId) return;

  if (isMockStarted && !isMockSubmitted && Object.keys(mockUserAnswers).length > 0) {
    if (!confirm("Başka bir deneme sınavına geçmek istediğinize emin misiniz? Mevcut işaretlemeleriniz sıfırlanacaktır.")) {
      return;
    }
  }

  currentMockExamId = examId;
  resetMockExam();
}

function initMockExam() {
  populateMockExamCards();
  renderOpticGrid();
  renderMockQuestion(0);
  updateMockTimerDisplay();

  const submitBtn = document.getElementById("btn-submit-mock");
  if (submitBtn) {
    submitBtn.addEventListener("click", finishMockExam);
  }
}

function startMockExam() {
  if (isMockSubmitted) return;
  isMockStarted = true;
  isMockPaused = false;

  document.getElementById("btn-start-mock").style.display = "none";
  document.getElementById("btn-pause-mock").style.display = "inline-block";
  document.getElementById("pause-mode-banner").style.display = "none";

  if (!mockTimerInterval) {
    mockTimerInterval = setInterval(() => {
      if (isMockStarted && !isMockPaused && !isMockSubmitted) {
        if (mockTimeRemaining > 0) {
          mockTimeRemaining--;
    if(mockTimeRemaining % 5 === 0) saveMockState();
          updateMockTimerDisplay();
        } else {
          clearInterval(mockTimerInterval);
          finishMockExam();
        }
      }
    }, 1000);
  }
}

function togglePauseMockExam() {
  if (!isMockStarted || isMockSubmitted) return;

  isMockPaused = !isMockPaused;
  const btn = document.getElementById("btn-pause-mock");
  const banner = document.getElementById("pause-mode-banner");

  if (isMockPaused) {
    btn.innerText = "▶️ Devam Et";
    btn.style.background = "rgba(245, 158, 11, 0.2)";
    btn.style.color = "#fbbf24";
    if (banner) banner.style.display = "block";
  } else {
    btn.innerText = "⏸️ Duraklat";
    btn.style.background = "";
    btn.style.color = "";
    if (banner) banner.style.display = "none";
  }
}

function resetMockExam() {
  clearInterval(mockTimerInterval);
  mockTimerInterval = null;

  mockUserAnswers = {};
    localStorage.removeItem("kpss_mock_state_" + examId);
  isMockStarted = false;
  isMockPaused = false;
  isMockSubmitted = false;
  mockTimeRemaining = 130 * 60;
  currentMockIndex = 0;

  document.getElementById("btn-start-mock").style.display = "inline-block";
  document.getElementById("btn-pause-mock").style.display = "none";
  document.getElementById("btn-pause-mock").innerText = "⏸️ Duraklat";
  document.getElementById("review-mode-banner").style.display = "none";
  document.getElementById("pause-mode-banner").style.display = "none";

  populateMockExamCards();
  updateMockTimerDisplay();
  renderOpticGrid();
  renderMockQuestion(0);
}

function updateMockTimerDisplay() {
  const mins = Math.floor(mockTimeRemaining / 60);
  const secs = Math.floor(mockTimeRemaining % 60);
  const clockEl = document.getElementById("mock-timer");
  if (clockEl) {
    clockEl.innerText = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  }
}

function jumpToMockQuestion(index) {
  const activeExam = getActiveMockExam();
  if (index >= 0 && index < activeExam.questions.length) {
    renderMockQuestion(index);
  }
}

function renderOpticGrid() {
  const container = document.getElementById("optic-grid-container");
  if (!container) return;

  const activeExam = getActiveMockExam();
  const totalQuestions = activeExam.questions.length;
  container.innerHTML = "";

  for (let i = 0; i < totalQuestions; i++) {
    const q = activeExam.questions[i];
    const userOpt = mockUserAnswers[q.id];
    const isAnswered = userOpt !== undefined;
    const isActive = i === currentMockIndex;

    const btn = document.createElement("div");
    let reviewClass = "";
    if (isMockSubmitted) {
      if (!isAnswered) reviewClass = "blank";
      else if (userOpt === q.correct) reviewClass = "correct";
      else reviewClass = "wrong";
    }

    btn.className = `optic-num ${isActive ? "active" : ""} ${isAnswered ? "answered" : ""} ${reviewClass}`;
    if (isMockSubmitted) {
      if (userOpt === q.correct) btn.style.background = "#10b981";
      else if (isAnswered) btn.style.background = "#f43f5e";
    }

    btn.innerText = i + 1;
    btn.onclick = () => renderMockQuestion(i);
    container.appendChild(btn);
  }
}

function renderMockQuestion(index) {
  currentMockIndex = index;
  renderOpticGrid();

  const container = document.getElementById("mock-question-display");
  const activeExam = getActiveMockExam();
  const q = activeExam.questions[index];
  if (!container || !q) return;

  const selectedOpt = mockUserAnswers[q.id];
  const isCorrectChoice = selectedOpt === q.correct;
  const isAnswered = selectedOpt !== undefined;

  let statusBadge = "";
  if (isMockSubmitted) {
    if (!isAnswered) {
      statusBadge = `<span style="background: rgba(245,158,11,0.2); color:#fbbf24; padding:6px 14px; border-radius:12px; font-weight:700; font-size:0.85rem;">⚪ Boş Bıraktınız (Doğru Cevap: ${String.fromCharCode(65 + q.correct)})</span>`;
    } else if (isCorrectChoice) {
      statusBadge = `<span style="background: rgba(16,185,129,0.2); color:#34d399; padding:6px 14px; border-radius:12px; font-weight:700; font-size:0.85rem;">✅ Doğru Yanıtladınız</span>`;
    } else {
      statusBadge = `<span style="background: rgba(244,63,94,0.2); color:#f87171; padding:6px 14px; border-radius:12px; font-weight:700; font-size:0.85rem;">❌ Yanlış Yanıtladınız (Doğru Cevap: ${String.fromCharCode(65 + q.correct)})</span>`;
    }
  }

  container.innerHTML = `
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 10px;">
      <span style="font-weight: 800; color: var(--accent-blue);">Soru ${index + 1} / ${activeExam.questions.length} [${q.subject}]</span>
      ${statusBadge}
    </div>

    <div class="question-text" style="font-size: 1.1rem; margin-bottom: 24px;">${q.text}</div>

    <div class="options-grid">
      ${q.options
        .map((opt, optIdx) => {
          let optionStyle = "";
          let tagText = "";

          if (isMockSubmitted) {
            if (optIdx === q.correct) {
              optionStyle = "correct";
              tagText = "✅ Doğru Cevap";
            } else if (optIdx === selectedOpt && selectedOpt !== q.correct) {
              optionStyle = "wrong";
              tagText = "❌ Sizin Yanıtınız";
            }
          } else {
            if (selectedOpt === optIdx) optionStyle = "selected";
          }

          return `
          <div class="option-pill ${optionStyle}" ${!isMockSubmitted ? `onclick="selectMockOption('${q.id}', ${optIdx})"` : ""}>
            <span>${opt}</span>
            ${tagText ? `<span style="font-weight:700; font-size:0.85rem;">${tagText}</span>` : ""}
          </div>
        `;
        })
        .join("")}
    </div>

    ${
      isMockSubmitted
        ? `
      <div style="margin-top: 24px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: var(--radius-md); padding: 18px; color: #a7f3d0; line-height: 1.6;">
        <b>📝 Detaylı Soru Çözümü:</b><br>
        ${q.solution}
      </div>
    `
        : ""
    }

    <div style="display: flex; justify-content: space-between; margin-top: 32px;">
      <button class="btn-solution" ${index === 0 ? "disabled style='opacity:0.5;'" : ""} onclick="renderMockQuestion(${index - 1})">⬅️ Önceki Soru</button>
      <button class="hero-cta" style="padding: 10px 20px; font-size: 0.9rem;" ${index === activeExam.questions.length - 1 ? "disabled style='opacity:0.5;'" : ""} onclick="renderMockQuestion(${index + 1})">Sonraki Soru ➡️</button>
    </div>
  `;
}

function selectMockOption(qId, optIdx) {
  if (isMockSubmitted) return;
  if (!isMockStarted) {
    startMockExam();
  }
  if (isMockPaused) {
    togglePauseMockExam();
  }

  mockUserAnswers[qId] = optIdx;
  renderMockQuestion(currentMockIndex);
}

function finishMockExam() {
  isMockSubmitted = true;
  isMockStarted = false;
  clearInterval(mockTimerInterval);
  if (typeof saveMockState === 'function') saveMockState();

  document.getElementById("btn-start-mock").style.display = "none";
  document.getElementById("btn-pause-mock").style.display = "none";

  const activeExam = getActiveMockExam();
  
  // Branş bazlı analiz nesnesi
  const stats = {
    "Türkçe": { d: 0, y: 0, b: 0, net: 0, total: 30 },
    "Matematik": { d: 0, y: 0, b: 0, net: 0, total: 30 },
    "Tarih": { d: 0, y: 0, b: 0, net: 0, total: 27 },
    "Coğrafya": { d: 0, y: 0, b: 0, net: 0, total: 18 },
    "Vatandaşlık": { d: 0, y: 0, b: 0, net: 0, total: 15 }
  };

  let totalD = 0, totalY = 0, totalB = 0;

  activeExam.questions.forEach((q) => {
    const userOpt = mockUserAnswers[q.id];
    const subj = q.subject;
    
    if (userOpt === undefined) {
      if(stats[subj]) stats[subj].b++;
      totalB++;
    } else if (userOpt === q.correct) {
      if(stats[subj]) stats[subj].d++;
      totalD++;
    } else {
      if(stats[subj]) stats[subj].y++;
      totalY++;
    }
  });

  let totalNet = 0;
  let tableHTML = `<table style="width:100%; border-collapse:collapse; margin-top:15px; text-align:center; background:#1e293b; border-radius:8px; overflow:hidden;">
    <tr style="background:#334155; color:#fff;">
      <th style="padding:10px;">Ders</th>
      <th>Soru</th>
      <th>Doğru</th>
      <th>Yanlış</th>
      <th>Boş</th>
      <th>Net</th>
    </tr>`;

  Object.keys(stats).forEach(subj => {
    const s = stats[subj];
    s.net = s.d - (s.y / 4);
    totalNet += s.net;
    tableHTML += `<tr style="border-bottom: 1px solid #334155;">
      <td style="padding:10px; font-weight:bold; text-align:left;">${subj}</td>
      <td>${s.total}</td>
      <td style="color:#4ade80;">${s.d}</td>
      <td style="color:#f87171;">${s.y}</td>
      <td style="color:#94a3b8;">${s.b}</td>
      <td style="color:#38bdf8; font-weight:bold;">${s.net.toFixed(2)}</td>
    </tr>`;
  });
  
  // P94 Puan Hesaplama (Yaklaşık formül)
  let p94 = 40 + (totalNet * 0.48);
  if (totalNet <= 0) p94 = 0;
  if (p94 > 100) p94 = 100;

  tableHTML += `<tr style="background:#0f172a; font-size:1.1em;">
      <td style="padding:12px; font-weight:bold; text-align:left;">TOPLAM</td>
      <td>120</td>
      <td style="color:#4ade80;">${totalD}</td>
      <td style="color:#f87171;">${totalY}</td>
      <td style="color:#94a3b8;">${totalB}</td>
      <td style="color:#38bdf8; font-weight:bold;">${totalNet.toFixed(2)}</td>
    </tr></table>`;

  const resultsDiv = document.getElementById("mock-results");
  resultsDiv.style.display = "block";
  
  resultsDiv.innerHTML = `
    <div style="text-align:center; margin-bottom:20px;">
      <h2 style="color:#facc15; font-size:2em; margin-bottom:5px;">Sınav Tamamlandı!</h2>
      <div style="background: linear-gradient(135deg, #10b981, #059669); color: white; display: inline-block; padding: 15px 30px; border-radius: 50px; font-size: 1.5em; font-weight: bold; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3); margin-top:10px;">
        Tahmini KPSS P94 Puanınız: ${p94.toFixed(3)}
      </div>
    </div>
    ${tableHTML}
    <div style="margin-top:20px; display:flex; gap:10px; justify-content:center;">
      <button class="btn" onclick="renderMockQuestion()">Yanıtları İncele</button>
      <button class="btn btn-next-mock-exam" onclick="goToNextMockExam()" id="btn-next-mock">Sıradaki Denemeye Geç</button>
    </div>
  `;

  renderMockGrid();
}

function goToNextMockExam() {
  document.getElementById("mock-result-modal").classList.remove("active");
  const exams = KPSS_DATA.mockExams || [KPSS_DATA.mockExam];
  const currentIdx = exams.findIndex((e) => (e.id || "") === currentMockExamId);
  const nextIdx = (currentIdx + 1) % exams.length;
  const nextExamId = exams[nextIdx].id || `deneme_${nextIdx + 1}`;
  changeMockExam(nextExamId);
  startMockExam();
}

function closeModal() {
  document.getElementById("mock-result-modal").classList.remove("active");
  renderMockQuestion(currentMockIndex);
}

/* 9. Global İstatistikleri Güncelleme */
function updateGlobalStats() {
  const answeredKeys = Object.keys(userAnswers);
  const totalSolved = answeredKeys.length;

  let correctCount = 0;
  answeredKeys.forEach((qId) => {
    for (let sub of KPSS_DATA.subjects) {
      for (let top of sub.topics) {
        const foundQ = top.questions.find((q) => q.id === qId);
        if (foundQ && userAnswers[qId] === foundQ.correct) {
          correctCount++;
        }
      }
    }
  });

  const accuracy = totalSolved > 0 ? Math.round((correctCount / totalSolved) * 100) : 0;

  document.getElementById("top-solved-count").innerText = totalSolved;
  if (document.getElementById("stat-total-solved")) {
    document.getElementById("stat-total-solved").innerText = totalSolved;
  }
  if (document.getElementById("stat-accuracy-rate")) {
    document.getElementById("stat-accuracy-rate").innerText = `%${accuracy}`;
  }

  // Tamamlanan Haftalar
  const checkedTaskCount = Object.values(checkedPlanTasks).filter(Boolean).length;
  const completedWeeksCount = Math.floor(checkedTaskCount / 3);
  if (document.getElementById("stat-completed-weeks")) {
    document.getElementById("stat-completed-weeks").innerText = `${completedWeeksCount} / 12`;
  }
}