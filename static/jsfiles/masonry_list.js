function masonryLayout() {
  const masonryContainerStyle = getComputedStyle(
      document.querySelector(".masonry-container")
  );
  const columnGap = parseInt(
      masonryContainerStyle.getPropertyValue("column-gap")
  );
  const autoRows = parseInt(
      masonryContainerStyle.getPropertyValue("grid-auto-rows")
  );

  document.querySelectorAll(".masonry-item").forEach((elt) => {
      elt.style.gridRowEnd = `span ${Math.ceil(
          elt.querySelector(".pseudo-img").scrollHeight / autoRows +
              columnGap / autoRows
      )}`;
  });
}

masonryLayout();
window.addEventListener("resize", masonryLayout);