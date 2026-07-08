// ===============================
// Zion Melodies Main JavaScript
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    // ===============================
    // Lucide Icons
    // ===============================
    if (typeof lucide !== "undefined") {
        lucide.createIcons();
    }

    // ===============================
    // Dark Mode Toggle
    // ===============================
    const body = document.body;
    const toggle = document.getElementById("dark-toggle");

    if (toggle) {
        toggle.addEventListener("click", () => {
            body.classList.toggle("dark");
            body.classList.toggle("light");

            localStorage.setItem(
                "theme",
                body.classList.contains("light") ? "light" : "dark"
            );
        });
    }

    const savedTheme = localStorage.getItem("theme");
    if (savedTheme === "light") {
        body.classList.remove("dark");
        body.classList.add("light");
    }

    // ===============================
    // Mobile Navigation
    // ===============================
    const menuBtn = document.getElementById("mobile-menu-btn");
    const mobileMenu = document.getElementById("mobile-menu");

    if (menuBtn && mobileMenu) {

        menuBtn.addEventListener("click", () => {
            mobileMenu.classList.toggle("hidden");
        });

        mobileMenu.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", () => {
                mobileMenu.classList.add("hidden");
            });
        });

    }

    // ===============================
    // Countdown Timer
    // Monday & Wednesday 6PM
    // ===============================
    function updateCountdown() {

        const now = new Date();

        const kenyaNow = new Date(
            now.toLocaleString("en-US", {
                timeZone: "Africa/Nairobi"
            })
        );

        const timer = document.getElementById("countdown-timer");

        if (!timer) return;

        let target = new Date(kenyaNow);

        const day = kenyaNow.getDay();
        const hour = kenyaNow.getHours();

        if (day === 1 && hour < 18) {

            target.setHours(18,0,0,0);

        } else if (day === 3 && hour < 18) {

            target.setHours(18,0,0,0);

        } else {

            let days;

            if (day < 1)
                days = 1 - day;
            else if (day < 3)
                days = 3 - day;
            else
                days = 8 - day;

            target.setDate(target.getDate() + days);
            target.setHours(18,0,0,0);

        }

        const diff = target - kenyaNow;

        if (diff <= 0) {

            timer.innerHTML = "🎵 In Progress";
            return;

        }

        const d = Math.floor(diff / 86400000);
        const h = Math.floor(diff % 86400000 / 3600000);
        const m = Math.floor(diff % 3600000 / 60000);
        const s = Math.floor(diff % 60000 / 1000);

        timer.innerHTML =
            `${d}d ${String(h).padStart(2,'0')}h ${String(m).padStart(2,'0')}m ${String(s).padStart(2,'0')}s`;

    }

    updateCountdown();

    setInterval(updateCountdown,1000);

    // ===============================
    // Contact Form
    // ===============================
    const form = document.getElementById("contact-form");

    if (form) {

        form.addEventListener("submit", async function(e){

            e.preventDefault();

            const submitBtn = document.getElementById("submit-btn");

            submitBtn.disabled = true;

            const data = {

                name: document.getElementById("name").value,
                email: document.getElementById("email").value,
                phone: document.getElementById("phone").value,
                message: document.getElementById("message").value

            };

            try{

                const response = await fetch("/contact/",{

                    method:"POST",

                    headers:{
                        "Content-Type":"application/json",
                        "X-CSRFToken":getCookie("csrftoken")
                    },

                    body:JSON.stringify(data)

                });

                const result = await response.json();

                if(result.success){

                    alert("Message sent successfully.");

                    form.reset();

                }else{

                    alert(result.error || "Unable to send message.");

                }

            }catch(err){

                alert("Server error.");

            }

            submitBtn.disabled = false;

        });

    }

    // ===============================
    // CSRF Helper
    // ===============================
    function getCookie(name){

        let cookieValue = null;

        if(document.cookie && document.cookie !== ""){

            const cookies = document.cookie.split(";");

            for(let i=0;i<cookies.length;i++){

                const cookie = cookies[i].trim();

                if(cookie.substring(0,name.length+1) === (name + "=")){

                    cookieValue = decodeURIComponent(cookie.substring(name.length+1));

                    break;

                }

            }

        }

        return cookieValue;

    }

});
