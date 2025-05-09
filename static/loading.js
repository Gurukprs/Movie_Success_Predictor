document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('prediction-form');
    const loader = document.getElementById('loader');
  
    form.addEventListener('submit', () => {
      loader.style.display = 'block';
    });
  });
  