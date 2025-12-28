console.log("✅ test2.js loaded");

function test2Action() {
    alert("This action is handled by Test App 2");
}

document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("test2-btn");
    if (btn) {
        btn.addEventListener("click", test2Action);
    }
});
