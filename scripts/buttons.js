all_buttons = Array.from(document.getElementsByTagName("button"));
let controls_buttons = [];

for (i of all_buttons) {
  if (i.id.slice(0, 3) == "btn") {
    controls_buttons.push(i);
  }
}

let btns = controls_buttons;

for (let btn of btns) {
  btn.addEventListener("touchstart", () => {
    down(btn);
    console.log(btn);
  });
  btn.addEventListener("touchend", () => up(btn));
  console.log(btns.indexOf(btn));
}

let interval;

function clickChecker() {
  for (btn of btns) {
    if (btn.innerHTML == "Down") {
      let url = "http://192.168.1.12:8000/buttons?data=p" + btn.value;
      Http.open("GET", url);
      Http.send();
    } else if (btn.innerHTML == "Up") {
      let url = "http://192.168.1.12:8000/buttons?data=r" + btn.value;
      Http.open("GET", url);
      Http.send();
    }
  }
}

const Http = new XMLHttpRequest();

function down(btn) {
  btn.innerHTML = "Down";

  interval = setInterval(clickChecker, 20);
}

function up(btn) {
  btn.innerHTML = "Up";

  clickChecker();
  btn.innerHTML = btn.id;
  clearInterval(interval);
}
