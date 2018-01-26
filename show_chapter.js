chapters_set = null;
current = null;

function show_chapter(id, scroll) {
  if (chapters_set.has(id)) {
    if (!scroll) {
      hide(current);
    }
    display(id);
  }
}

function display(id) {
  document.getElementById(id).style.display = 'block';
  current = id;
}

function hide(id) {
  document.getElementById(id).style.display = 'none';
}

function chapters(all) {
  current = all[0];
  chapters_set = new Set(all);
}