document.addEventListener("DOMContentLoaded", function() {
    const tocToggle = document.getElementById("toc-toggle");
    const tocContent = document.getElementById("toc-content");

    tocToggle.addEventListener("click", function() {
        if (tocContent.style.display === "none" || tocContent.style.display === "") {
            tocContent.style.display = "block";
            tocToggle.textContent = "Hide Table of Contents";
        } else {
            tocContent.style.display = "none";
            tocToggle.textContent = "Table of Contents";
        }
    });
});
