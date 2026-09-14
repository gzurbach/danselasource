// Mobile nav + photo lightbox. No dependencies.
(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    var sync = function () {
      var wide = window.matchMedia("(min-width: 48rem)").matches;
      if (wide) {
        nav.hidden = false;
        toggle.setAttribute("aria-expanded", "false");
      } else if (toggle.getAttribute("aria-expanded") !== "true") {
        nav.hidden = true;
      }
    };
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      nav.hidden = open;
    });
    window.addEventListener("resize", sync);
    sync();
  }

  var lb = document.getElementById("lightbox");
  if (!lb) {
    return;
  }

  var shots = [].slice.call(document.querySelectorAll("[data-shot]"));
  if (!shots.length) {
    return;
  }

  var img = lb.querySelector(".lb-img img");
  var cap = lb.querySelector(".lb-cap");
  var count = lb.querySelector(".lb-count");
  var at = 0;
  var opener = null;

  function show(i) {
    at = (i + shots.length) % shots.length;
    var btn = shots[at];
    img.src = btn.getAttribute("data-shot");
    img.alt = btn.getAttribute("data-alt") || "";
    cap.textContent = btn.getAttribute("data-alt") || "";
    count.textContent = at + 1 + " / " + shots.length;
  }

  function open(i) {
    opener = document.activeElement;
    show(i);
    lb.hidden = false;
    document.body.style.overflow = "hidden";
    lb.querySelector(".lb-close").focus();
  }

  function close() {
    lb.hidden = true;
    document.body.style.overflow = "";
    img.src = "";
    if (opener && opener.focus) {
      opener.focus();
    }
  }

  shots.forEach(function (btn, i) {
    btn.addEventListener("click", function () {
      open(i);
    });
  });

  lb.querySelector(".lb-close").addEventListener("click", close);
  lb.querySelector(".lb-prev").addEventListener("click", function () {
    show(at - 1);
  });
  lb.querySelector(".lb-next").addEventListener("click", function () {
    show(at + 1);
  });
  lb.addEventListener("click", function (e) {
    if (e.target === lb || e.target.classList.contains("lb-img")) {
      close();
    }
  });

  document.addEventListener("keydown", function (e) {
    if (lb.hidden) {
      return;
    }
    if (e.key === "Escape") {
      close();
    } else if (e.key === "ArrowLeft") {
      show(at - 1);
    } else if (e.key === "ArrowRight") {
      show(at + 1);
    }
  });

  // Swipe between photos on touch screens.
  var x0 = null;
  lb.addEventListener("touchstart", function (e) {
    x0 = e.changedTouches[0].clientX;
  }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    if (x0 === null) {
      return;
    }
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 45) {
      show(dx < 0 ? at + 1 : at - 1);
    }
    x0 = null;
  }, { passive: true });
})();
