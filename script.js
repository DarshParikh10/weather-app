document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("dark-mode-toggle");
    const body = document.body;

    // 🌙 Toggle Dark Mode & Save Preference
    toggleBtn.addEventListener("click", function () {
        body.classList.toggle("dark-mode");
        localStorage.setItem("darkMode", body.classList.contains("dark-mode"));
    });

    // 🌙 Load Saved Theme
    if (localStorage.getItem("darkMode") === "true") {
        body.classList.add("dark-mode");
    }

    // ⏳ Live Time & Date
    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString();
        const dateString = now.toDateString();
        document.getElementById("current-time").innerHTML = `${dateString} | ${timeString}`;
    }
    setInterval(updateTime, 1000);
    updateTime();
});
