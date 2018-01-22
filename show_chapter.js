chapters_set = null;

function show_chapter(id) {
  if (chapters_set.has(id)) {
    document.getElementById(id).style.display = 'block';
  }
}

function chapters(all) {
  chapters_set = new Set(all);
}