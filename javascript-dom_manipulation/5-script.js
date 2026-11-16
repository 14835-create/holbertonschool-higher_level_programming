const header = document.querySelector('header');
const updateDiv = document.querySelector('#update_header');

updateDiv.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
