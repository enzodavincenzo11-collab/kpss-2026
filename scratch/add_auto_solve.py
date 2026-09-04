import sys, re
sys.stdout.reconfigure(encoding='utf-8')

APP_PATH = r'c:\Users\oktay\Desktop\kpss\app.js'
INDEX_PATH = r'c:\Users\oktay\Desktop\kpss\index.html'

# 1. app.js'e autoSolveCurrentMockExam fonksiyonu ekle
with open(APP_PATH, 'r', encoding='utf-8') as f:
    app_js = f.read()

auto_solve_func = """
// --- TEST & SİMÜLASYON: 120 SORUYU TEK TIKLA ÇÖZ ---
function autoSolveCurrentMockExam() {
  const activeExam = getActiveMockExam();
  if (!activeExam || !activeExam.questions) return;

  isMockStarted = true;
  isMockSubmitted = false;
  mockUserAnswers = {};
  mockTimeRemaining = 24 * 60; // Kalan süre 24 dk
  
  const startBtn = document.getElementById("btn-start-mock");
  if (startBtn) startBtn.style.display = "none";
  const pauseBtn = document.getElementById("btn-pause-mock");
  if (pauseBtn) pauseBtn.style.display = "inline-block";

  activeExam.questions.forEach((q, idx) => {
    // 4 boş bırakalım: 29, 59, 86, 120
    if (idx === 28 || idx === 58 || idx === 85 || idx === 119) {
      return;
    }
    // 8 soruda çeldiriciye takılalım (gerçekçi öğrenci performansı):
    if ([11, 23, 44, 51, 69, 79, 94, 109].includes(idx)) {
      mockUserAnswers[q.id] = (q.correct + 1) % 5;
    } else {
      mockUserAnswers[q.id] = q.correct;
    }
  });

  if (typeof saveMockState === 'function') saveMockState();
  updateMockTimerDisplay();
  renderOpticGrid();
  renderMockQuestion(currentMockIndex || 0);
  
  if (typeof showToast === 'function') {
    showToast("120 soru yapay zeka tarafından çözüldü! 'Sınavı Bitir'e basabilirsiniz.", "info");
  }
}
"""

if "autoSolveCurrentMockExam" not in app_js:
    app_js += "\n" + auto_solve_func
    with open(APP_PATH, 'w', encoding='utf-8') as f:
        f.write(app_js)
    print("app.js'e autoSolveCurrentMockExam fonksiyonu eklendi.")

# 2. index.html'deki sayaç barına test çözme butonu ekle
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

if "btn-auto-solve" not in html:
    btn_markup = '<button id="btn-auto-solve" class="btn-solution" style="background: rgba(59, 130, 246, 0.2); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.4); font-weight: 700;" onclick="autoSolveCurrentMockExam()">⚡ 120 Soruyu Otomatik Çöz (Test)</button>\n                '
    html = html.replace('<button id="btn-finish-timer-bar"', btn_markup + '<button id="btn-finish-timer-bar"')
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html'e '⚡ 120 Soruyu Otomatik Çöz (Test)' butonu eklendi.")

print("İşlem tamam!")
