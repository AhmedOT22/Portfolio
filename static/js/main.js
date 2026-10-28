/* Progressive enhancement: all projects and navigation work without JavaScript. */
const toolbar = document.querySelector(".project-toolbar");
if (toolbar) {
  const buttons = [...toolbar.querySelectorAll("[data-filter]")];
  const cards = [...document.querySelectorAll(".project-card")];
  const count = toolbar.querySelector(".project-count");
  toolbar.hidden = false;
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const selected = button.dataset.filter;
      buttons.forEach((item) =>
        item.setAttribute("aria-pressed", String(item === button)),
      );
      let visible = 0;
      cards.forEach((card) => {
        card.hidden =
          selected !== "All projects" && card.dataset.category !== selected;
        if (!card.hidden) visible += 1;
      });
      count.textContent = `${visible} ${visible === 1 ? "project" : "projects"}`;
    });
  });
}
