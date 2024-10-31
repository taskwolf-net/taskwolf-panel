window.addEventListener('load', function () {
  if (Cookie.find("dulno-theme") == null) {
    Cookie.create("dulno-theme", "dark", 60 * 60 * 24 * 365, ".dulno.com");
  }
  let theme = Cookie.find("dulno-theme");
  var logoSource;
  if (theme === "dark") {
    document.body.classList.add("dark");
    document.body.setAttribute("data-bs-theme", "dark");
    logoSource = "logo-light.webp";
  } else {
    document.body.classList.remove("dark");
    document.body.classList.add("light");
    document.body.setAttribute("data-bs-theme", "light");
    logoSource = "logo-dark.webp";
  }
  var logoElements = document.getElementsByClassName("dulno-logo");
  for (var i = 0; i < logoElements.length; i++) {
    logoElements[i].src = "https://dulno.com/static/img/" + logoSource;
  }
});