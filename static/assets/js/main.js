/**
* Template Name: Eterna - v4.6.0
* Template URL: https://bootstrapmade.com/eterna-free-multipurpose-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

// Licencias
if(window.location.pathname == "/mi-cv/editar/otros"){
  const licenciaNoPosee = document.querySelector("#NoPosee");

  window.addEventListener('DOMContentLoaded', (event) => {
    if(licenciaNoPosee.checked){
      document.querySelector('.tipo-licencias').remove();
    }
  });

  licenciaNoPosee.addEventListener('change', function() {
    if (this.checked) {
      document.querySelector('.tipo-licencias').remove();
    } else {
      const tipoLicencias = `
                          <div class="row">
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="A1" name="licencia">
                                      <label class="form-check-label" for="A1">
                                        A1
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="A2" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        A2
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="A2.1" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        A2.1
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="A2.2" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        A2.2
                                      </label>
                                  </div>
                              </div>
                          </div>
                          
                          <div class="row">
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="A3" name="licencia">
                                      <label class="form-check-label" for="A1">
                                        A3
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="B1" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        B1
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="B2" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        B2
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="C1" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        C1
                                      </label>
                                  </div>
                              </div>
                          </div>

                              <div class="row">
                                  <div class="col-1">
                                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="C2" name="licencia" name="A1">
                                          <label class="form-check-label" for="A1">
                                            C2
                                          </label>
                                      </div>
                                  </div>
                                  <div class="col-1">
                                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="C3" name="licencia">
                                          <label class="form-check-label" for="defaultCheck1">
                                            C3
                                          </label>
                                      </div>
                                  </div>
                                  <div class="col-1">
                                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="D1" name="licencia">
                                          <label class="form-check-label" for="defaultCheck1">
                                            D1
                                          </label>
                                      </div>
                                  </div>
                                  <div class="col-1">
                                      <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="D2" name="licencia">
                                          <label class="form-check-label" for="defaultCheck1">
                                            D2
                                          </label>
                                      </div>
                                  </div>
                              </div>

                          <div class="row">
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="D3" name="licencia">
                                      <label class="form-check-label" for="A1">
                                        D3
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="D4" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        D4
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="E1" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        E1
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="E2" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        E2
                                      </label>
                                  </div>
                              </div>
                          </div>
                          <div class="row">
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="F" name="licencia">
                                      <label class="form-check-label" for="A1">
                                        F
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="G1" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        G1
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="G2" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        G2
                                      </label>
                                  </div>
                              </div>
                              <div class="col-1">
                                  <div class="form-check">
                                      <input class="form-check-input" type="checkbox" value="G3" name="licencia">
                                      <label class="form-check-label" for="defaultCheck1">
                                        G3
                                      </label>
                                  </div>
                              </div>
                          </div>
      `;

      const listaLicencias = document.createElement('div');
      listaLicencias.classList.add('tipo-licencias');
      listaLicencias.innerHTML = tipoLicencias;
      document.querySelector('.licencias').appendChild(listaLicencias);

    }
  });
}


(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 16
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Header fixed top on scroll
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    let headerOffset = selectHeader.offsetTop
    let nextElement = selectHeader.nextElementSibling
    const headerFixed = () => {
      if ((headerOffset - window.scrollY) <= 0) {
        selectHeader.classList.add('fixed-top')
        nextElement.classList.add('scrolled-offset')
      } else {
        selectHeader.classList.remove('fixed-top')
        nextElement.classList.remove('scrolled-offset')
      }
    }
    window.addEventListener('load', headerFixed)
    onscroll(document, headerFixed)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Hero carousel indicators
   */
  let heroCarouselIndicators = select("#hero-carousel-indicators")
  let heroCarouselItems = select('#heroCarousel .carousel-item', true)

  heroCarouselItems.forEach((item, index) => {
    (index === 0) ?
    heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "' class='active'></li>":
      heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "'></li>"
  });

  /**
   * Clients Slider
   */
  new Swiper('.clients-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120
      }
    }
  });

  /**
   * Skills animation
   */
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function(direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%'
        });
      }
    })
  }

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item',
        layoutMode: 'fitRows'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

})()

// ==========================================================
  
// Formatear fecha
function formatear_fecha(fecha) {
  año = fecha[0]
  dia = fecha[2]

  if(fecha[1] == 1){
      mes = "enero"
  }
  if(fecha[1] == 2){
      mes = "febrero"
  }
  if(fecha[1] == 3){
      mes = "marzo"
  }
  if(fecha[1] == 4){
      mes = "abril"
  }
  if(fecha[1] == 5){
      mes = "mayo"
  }
  if(fecha[1] == 6){
      mes = "julio"
  }
  if(fecha[1] == 7){
      mes = "junio"
  }
  if(fecha[1] == 8){
      mes = "agosto"
  }
  if(fecha[1] == 9){
      mes = "septiembre"
  }
  if(fecha[1] == 10){
      mes = "octubre"
  }
  if(fecha[1] == 11){
      mes = "noviembre"
  }
  if(fecha[1] == 12){
      mes = "diciembre"
  }

  return `${dia} de ${mes} de ${año}`

}
fecha_nacimiento = document.querySelector("#fechanacimiento").innerHTML.split('-')
fecha_formateada = formatear_fecha(fecha_nacimiento)
document.querySelector("#fechanacimiento").innerHTML = fecha_formateada

// Sueldo no especificado
if(document.querySelector('input[name="sueldo"]') !== undefined){

  const sueldoNoEspecifica = document.querySelector('#NoEspecificado');

  window.addEventListener('DOMContentLoaded', (event) => {
    if(sueldoNoEspecifica.checked){
      document.querySelector('.sueldo').innerHTML = '<input type="hidden" name="sueldo" value="0"></input>';
    }
  });

  sueldoNoEspecifica.addEventListener('change', function(){
    
    if(this.checked){
      document.querySelector('.sueldo').innerHTML = '<input type="hidden" name="sueldo" value="0"></input>';
    } else {
      document.querySelector('.sueldo').innerHTML = '<input type="text" class="form-control" name="sueldo" placeholder="Sueldo del puesto" value="">';
    }

  })

}