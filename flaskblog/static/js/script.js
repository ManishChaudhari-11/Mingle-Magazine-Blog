// Function to set the active link based on the current URL and category
function setActiveLink() {
  const currentPathname = window.location.pathname;
  const currentCategory = getUrlParam("category");

  const menuItems = document.querySelectorAll("#mylist a");

  menuItems.forEach((item) => {
    const href = item.getAttribute("href");
    const itemCategory = getUrlParam("category", href);

    if (currentPathname === href && currentCategory === itemCategory) {
      item.classList.add("active");
    } else {
      item.classList.remove("active");
    }
  });
}

// Function to get a URL parameter from the current URL
function getUrlParam(param, url) {
  const queryString = url
    ? url.split("?")[1] || ""
    : window.location.search.substring(1);
  const urlSearchParams = new URLSearchParams(queryString);

  // Check if the parameter is "None" and return an empty string
  if (urlSearchParams.has(param)) {
    const paramValue = urlSearchParams.get(param);
    return paramValue === "None" ? "" : paramValue;
  }

  return "";
}

// Call the function to set the active link when the page loads
setActiveLink();
