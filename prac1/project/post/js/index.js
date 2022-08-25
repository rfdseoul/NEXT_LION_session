

const $ = (selector) => document.querySelector(selector);
const body = $("body");
const modal = $(".modal-container");


const openModal = () => {
    modal.classList.add("open");
    body.style.overflow = "hidden";
  }

const closeModal = () => {
    modal.classList.remove("open");
    body.style.overflow = "auto";
  }

// 📁 cookie.js
// 쿠키 관련 함수들을 저장하고 내보낸다.

// 만료기한을 정해 쿠키 생성하기
const setCookie = (name, value, expireDays) => {
  // 현재 날짜와 시간이 저장된 Date 객체 생성하기
  let data = new Date();
  // 오늘 날짜에 expireDays만큼 더해서 만료시간을 구하기
  date.setDate(date.getDate()+expiresDays);
  // 쿠키 생성하기 (템플릿 리터럴 활용)
  document.cookie = `${name}=${value}; expires=${date.toUTCstring()}`;
};

// 특정 이름의 쿠키를 가져오기
const getCookie = (name) => {
  // 로컬에 저장된 모든 쿠키 읽어오기
  let cookie = document.cookie;
  // 로컬에 저장된 쿠키가 존재하면 쿠키를 배열에 저장해서 배열을 순회하며 내가 원하는 이름의 쿠키를 리턴하기
  if (document.cookie) {
    let cookieArray = cookie.split("; ");
    // 배열을 순회하면서 쿠키의 name에 대한 value값을 리턴 (반복문)
    console.log(cookieArray);
    for(let index in cookieArray) {
      let cookieName = cookieArray[index].split("=");
      if(cookieName[0] === name) {
        return cookieNmae[1];
      }
    }
  }
  return;
};


function App() {
  this.init = () => {
    //스케줄 불러오는 함수를 호출해 첫 페이지 렌더링시 화면에 보여준다.
    renderScheudule();
    // 모달을 닫는 쿠키가 있는지 확인한다.
    if(getCookie('modalClose') === true) {
      closeModal();
      return;
    }
    // 모달을 닫는 쿠기가 없다면 무조건 모달을 열어둔다.
    openModal();
  };

  // 오늘 보지 않음 버튼을 눌렀을 때 쿠키를 만들고 모달을 닫기

  $(".modal-stop-button").addEventListener("click", () => {
    setCookie("modalClose", "true", 1);
    closeModal();
  });

  $(".modal-open").addEventListener("click", () => {
    openModal();
  });

  $(".modal-close").addEventListener("click", () => {
    closeModal();
  });

  $(".modal-container").addEventListener("click", (event) => {
    if(event.target === $(".modal-container")) {
      closeModal();
    }
  });
}

// 페이지 최초로 접근했을 때 app 이라는 객체를 생성한다.
// new 연산자로 생성된 인스턴스는 하나의 라이프사이클을 가지고, 이거에 대한 개별적인 상태 관리가 가능해진다.
const app = new App();
// 그 app의 init이라는 메소드를 불러와서 로직을 실행될 수 있게끔 한다.
app.init();