(function () {
  "use strict";

  function init() {
    id("btn-input").addEventListener("keypress", (e) => {
      if (e.keyCode == 13) {
        clickChat();
        e.preventDefault();
      }
    });
  }

  function clickChat() {
    let input = id("btn-input");
    let text = input.value;
    if (text.length > 0) {
      insertChat("You", text);
      input.value = "";
      fetch(`./chat?data=${encodeURIComponent(text)}`, { method: "GET"})
        .then(response => response.json())
        .then(data => insertChat(data["name"], data["response"]));
    }
  }

  function insertChat(user, text) {
    // blargh
    let chat = `<li><strong class="primary-font chat-name">${user}</strong>: <span class="chat-body">${text}</span></li>`;
    id("chat-list").append((new DOMParser().parseFromString(chat, "text/html")).body);
  }

  /**
   * Returns the element that has the ID attribute with the specified value.
   * @param {string} idName - element ID
   * @returns {object} DOM object associated with id.
   */
  function id(idName) {
    return document.getElementById(idName);
  }

    /**
   * Returns a new element with the given tagname
   * @param {string} tagname - name of element to create and return
   * @returns {object} new DOM element with the given tagname
   */
     function gen(tagname) {
      return document.createElement(tagname);
    }

  init();
})();
