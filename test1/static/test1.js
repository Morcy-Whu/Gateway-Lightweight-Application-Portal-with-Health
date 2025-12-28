console.log("✅ test1.js loaded");

function test1Action() {
    alert("This action is handled by Test App 1");
}

// 页面加载完成后执行
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("test1-btn");
    if (btn) {
        btn.addEventListener("click", test1Action);
    }
});
