$(".top-slider__inner").slick({
  dots: true,
  arrows: false,
  fade: true,
  autoplay: true,
});

$(".selling__products--slider").slick({
  prevArrow:
    '<button type="button" class="slick-prev"><svg width="10" height="18" viewBox="0 0 10 18" fill="none" xmlns="http://www.w3.org/2000/svg">  <path fill-rule="evenodd" clip-rule="evenodd" d="M9.63388 0.616117C10.122 1.10427 10.122 1.89573 9.63388 2.38388L3.01777 9L9.63388 15.6161C10.122 16.1043 10.122 16.8957 9.63388 17.3839C9.14573 17.872 8.35427 17.872 7.86612 17.3839L0.366117 9.88388C-0.122039 9.39573 -0.122039 8.60427 0.366117 8.11612L7.86612 0.616117C8.35427 0.127961 9.14573 0.127961 9.63388 0.616117Z" fill="#fff"/>   </svg> </button>',
  nextArrow:
    '<button type="button" class="slick-next"><svg width="10" height="18" viewBox="0 0 10 18" fill="none" xmlns="http://www.w3.org/2000/svg">  <path fill-rule="evenodd" clip-rule="evenodd" d="M0.366117 0.616117C0.854272 0.127961 1.64573 0.127961 2.13388 0.616117L9.63388 8.11612C10.122 8.60427 10.122 9.39573 9.63388 9.88388L2.13388 17.3839C1.64573 17.872 0.854272 17.872 0.366117 17.3839C-0.122039 16.8957 -0.122039 16.1043 0.366117 15.6161L6.98223 9L0.366117 2.38388C-0.122039 1.89573 -0.122039 1.10427 0.366117 0.616117Z" fill="#fff"/>  </svg> </button>',
  lazyLoad: "ondemand",
  slidesToShow: 4,
  slidesToScroll: 1,
});

const tabsContainer = document.querySelector(".tabs-container");
const tabsList = tabsContainer.querySelector("ul");
const tabButtons = tabsList.querySelectorAll("a");
const tabPanels = tabsContainer.querySelectorAll(".tabs__panels > div");

tabsList.setAttribute("role", "tablist");

tabsList.querySelectorAll("li").forEach((listitem) => {
  listitem.setAttribute("role", "presentation");
});

tabButtons.forEach((tab, index) => {
  tab.setAttribute("role", "tab");
  if (index === 0) {
    tab.setAttribute("aria-selected", "true");
    // we'll add something here
  } else {
    tab.setAttribute("tabindex", "-1");
    tabPanels[index].setAttribute("hidden", "");
  }
});

tabPanels.forEach((panel) => {
  panel.setAttribute("role", "tabpanel");
  panel.setAttribute("tabindex", "0");
});

tabsContainer.addEventListener("click", (e) => {
  const clickedTab = e.target.closest("a");
  if (!clickedTab) return;
  e.preventDefault();

  switchTab(clickedTab);
});

tabsContainer.addEventListener("keydown", (e) => {
  switch (e.key) {
    case "ArrowLeft":
      moveLeft();
      break;
    case "ArrowRight":
      moveRight();
      break;
    case "Home":
      e.preventDefault();
      switchTab(tabButtons[0]);
      break;
    case "End":
      e.preventDefault();
      switchTab(tabButtons[tabButtons.length - 1]);
      break;
  }
});

function moveLeft() {
  const currentTab = document.activeElement;
  if (!currentTab.parentElement.previousElementSibling) {
    switchTab(tabButtons[tabButtons.length - 1]);
  } else {
    switchTab(
      currentTab.parentElement.previousElementSibling.querySelector("a")
    );
  }
}

function moveRight() {
  const currentTab = document.activeElement;
  if (!currentTab.parentElement.nextElementSibling) {
    switchTab(tabButtons[0]);
  } else {
    switchTab(currentTab.parentElement.nextElementSibling.querySelector("a"));
  }
}

function switchTab(newTab) {
  const activePanelId = newTab.getAttribute("href");
  const activePanel = tabsContainer.querySelector(activePanelId);

  tabButtons.forEach((button) => {
    button.setAttribute("aria-selected", false);
    button.setAttribute("tabindex", "-1");
  });

  tabPanels.forEach((panel) => {
    panel.setAttribute("hidden", true);
  });

  activePanel.removeAttribute("hidden", false);

  newTab.setAttribute("aria-selected", true);
  newTab.setAttribute("tabindex", "0");
  newTab.focus();
}
