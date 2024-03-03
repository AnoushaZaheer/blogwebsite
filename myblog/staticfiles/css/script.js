let slideIndex = 0;

function moveSlide(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  let i;
  const slides = document.getElementsByClassName("slide");
  if (n >= slides.length) {
    slideIndex = 0;
  }
  if (n < 0) {
    slideIndex = slides.length - 1;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex].style.display = "flex";
}

function startSlider() {
  showSlides(slideIndex);
  slideIndex++;
}

setInterval(startSlider, 2000); // Change slide every 5 seconds

// Previous and next button functionality
document.querySelector(".prev").addEventListener("click", function() {
  moveSlide(-1);
});

document.querySelector(".next").addEventListener("click", function() {
  moveSlide(1);
});


function toggleSearch() {
  var overlay = document.getElementById('search-overlay');
  overlay.style.display === 'none' ? overlay.style.display = 'flex' : overlay.style.display = 'none';
}

function closeSearch() {
  var overlay = document.getElementById('search-overlay');
  overlay.style.display = 'none';
}

