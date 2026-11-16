const header = document.querySelector('header');
const toggleDiv = document.querySelector('#toggle_header');

toggleDiv.addEventListener('click', () => {
  if (header.classList.contains('red')) {
  } else {
    header.classList.replace('green', 'red');
  }
});
