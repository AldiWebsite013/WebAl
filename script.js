let countdownInterval;

async function fetchTimer() {
  const res = await fetch("https://your-backend.onrender.com/get_timer");
  const data = await res.json();

  if (data.end_time) {
    startCountdown(new Date(data.end_time));
  }
}

async function startTimer() {
  await fetch("https://your-backend.onrender.com/start_timer", { method: "POST" });
  fetchTimer();
}

function startCountdown(endTime) {
  clearInterval(countdownInterval);

  countdownInterval = setInterval(() => {
    const now = new Date();
    const distance = endTime - now;

    if (distance < 0) {
      clearInterval(countdownInterval);
      document.getElementById("timer").textContent = "Waktu Habis!";
    } else {
      const seconds = Math.floor(distance / 1000);
      document.getElementById("timer").textContent = `${seconds} detik tersisa`;
    }
  }, 1000);
}

document.getElementById("startBtn").addEventListener("click", startTimer);

fetchTimer(); // Saat halaman dibuka, ambil waktu dari backend
