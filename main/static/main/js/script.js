document.addEventListener('DOMContentLoaded', function() {
  var formLink = document.getElementById('formLink');
  formLink.addEventListener('click', function(event) {
    event.preventDefault(); // Предотвращаем переход по ссылке

    var key = prompt("Введите специальный ключ:");

    // Здесь "expected_key" - это значение, которое вы ожидаете от пользователя
    var expected_key = "key";

    if (key === expected_key) {
      // Если ключ верный, перенаправить пользователя на форму
      window.location.href = formLink.getAttribute('href');
    } else {
      // Если ключ неверный, ничего не делать или показать сообщение об ошибке
      alert("Неверный ключ!");
    }
  });
});
