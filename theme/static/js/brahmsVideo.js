function setupBrahmsVideo() {
    const videoElement = document.getElementById("brahms-video");

    if (videoElement) {
        videoElement.removeEventListener("mouseenter", function() { videoElement.play() }) // Remove first to avoid duplicates
        videoElement.removeEventListener("mouseleave", function() { videoElement.pause() })
        videoElement.addEventListener("mouseenter", function() { videoElement.play() })
        videoElement.addEventListener("mouseleave", function() { videoElement.pause() })
    }
}

setupBrahmsVideo()

// Re-run setup functions after SPA navigation
document.addEventListener("nav", () => {
    setupBrahmsVideo()
})