/* app.js */

document.addEventListener('DOMContentLoaded', function() {
    console.log("Custom JS loaded successfully.");
  
    // ================================================================
    // Validación personalizada de formularios (Bootstrap)
    // ================================================================
    (function() {
      'use strict';
      var forms = document.querySelectorAll('.needs-validation');
      Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
          if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
          }
          form.classList.add('was-validated');
        }, false);
      });
    })();
  
    // ================================================================
    // Smooth scrolling para anclas internas (opcional)
    // ================================================================
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  
    // ================================================================
    // Efecto fade-in para elementos con la clase .fade-in
    // ================================================================
    const fadeInElements = document.querySelectorAll('.fade-in');
    fadeInElements.forEach((el, index) => {
      setTimeout(() => {
        el.classList.add('visible');
      }, 500 * index);
    });
  
    // ================================================================
    // Ejemplo de funcionalidad adicional: alerta de bienvenida
    // ================================================================
    const welcomeAlert = document.querySelector('#welcomeAlert');
    if (welcomeAlert) {
      setTimeout(() => {
        welcomeAlert.classList.add('show');
      }, 1000);
    }
  
    // ================================================================
    // Función para mostrar el scroll de "volver arriba" (opcional)
    // ================================================================
    const backToTopBtn = document.getElementById('backToTop');
    if (backToTopBtn) {
      window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
          backToTopBtn.classList.add('visible');
        } else {
          backToTopBtn.classList.remove('visible');
        }
      });
      backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }
  
    // ================================================================
    // Más funciones personalizadas pueden agregarse aquí
    // ================================================================
  });
  