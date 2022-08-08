import { openModal, closeModal } from "./modal.js";

const $ = (selector) => document.querySelector(selector);

const body = $("body");
const modal = $(".modal-container");


const openModal = () => {
    modal.classList.add("open");
  }

const closeModal = () => {
    modal.classList.remove("open");
    body.style.overflow = "auto";
  }


$(".open-modal").addEventListener("click", () => {
    openModal();
  });

$(".close-modal").addEventListener("click", () => {
    closeModal();
  });

$(".modal-container").addEventListener("click", (event) => {
    if(event.target === $(".modal-container")) {
      closeModal();
    }
  });
