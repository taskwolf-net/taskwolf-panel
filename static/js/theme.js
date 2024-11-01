window.addEventListener('load', function () {
  let url = window.location.href.replace("https://panel.dulno.com/", "").replaceAll("/", "");
  if (url === "") {
    return;
  }
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
  let logoElements = document.getElementsByClassName("dulno-logo");
  for (let i = 0; i < logoElements.length; i++) {
    logoElements[i].src = "https://dulno.com/static/img/" + logoSource;
  }
  for (let themeButton of document.getElementsByClassName("btn-theme")) {
    if (theme === "light") {
      themeButton.classList.remove("btn-secondary");
      themeButton.classList.add("btn-light");
    }
  }
});