function sayHello () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(result => {
      if (!(result.ok)) {
        throw new Error('not allowed!');
      }
      return result.json();
    })
    .then(data => {
      const dataRead = document.getElementById('hello');
      dataRead.innerHTML = data.hello;
    })
    .catch(new Error('not allowed!'));
}
sayHello();
