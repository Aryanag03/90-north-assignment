

const resizeBtn = document.querySelector("[data-resize-btn]");

resizeBtn.addEventListener("click", function (e) {
  e.preventDefault();
  // Toggle the `sb-expanded` class only for the left sidebar
  document.body.classList.toggle("left-expanded");
});

// Function to adjust page size and ensure it fits within the viewport
function adjustPageSize() {
  const width = window.innerWidth; // Get the current window width
  const height = window.innerHeight; // Get the current window height

  // Reset scale and transform styles for the page
  document.body.style.transform = 'scale(1)';
  document.body.style.transformOrigin = 'top left';

  // Calculate scaling factor based on width
  let scaleFactor = 1;

  if (width >= 992 && width <= 1600) {
      scaleFactor = 0.9; // Shrink to 90%
  } else if (width >= 700 && width <= 767) {
      scaleFactor = 0.8; // Shrink to 80%
  } else if (width >= 600 && width < 700) {
      scaleFactor = 0.75; // Shrink to 75%
  } else if (width <= 600) {
      scaleFactor = 0.5; // Shrink to 50%
  }

  // Apply the calculated scale factor
  document.body.style.transform = `scale(${scaleFactor})`;

  // Ensure the page always fits within the viewport without scrolling
  document.body.style.width = `${width / scaleFactor}px`; 
  document.body.style.height = `${height / scaleFactor}px`;
}

// Run the function on page load
window.onload = adjustPageSize;

// Add an event listener to handle window resizing
window.onresize = adjustPageSize;
