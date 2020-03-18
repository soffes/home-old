class CameraCard extends HTMLElement {
  set hass(hass) {
    if (!this.content) {
      const card = document.createElement('ha-card');
      this.content = document.createElement('div');
      this.content.style.paddingTop = '56.25%';
      this.content.style.position = 'relative';
      card.appendChild(this.content);
      this.appendChild(card);
    }

    const href = this.config.camera_url;
    const src = hass.states[this.config.entity].attributes.entity_picture;

    this.content.innerHTML = `
      <a href="${href}" target="_blank" style="display:block;position:absolute;top:0;left:0;">
        <img src="${src}" style="width:100%">
      </a>`;
  }

  setConfig(config) {
    if (!config.entity) {
      throw new Error('You need to define entity');
    }

    if (!config.camera_url) {
      throw new Error('You need to define camera_url');
    }

    this.config = config;
  }

  // The height of your card. Home Assistant uses this to automatically
  // distribute all cards over the available columns.
  getCardSize() {
    return 3;
  }
}

customElements.define('camera-card', CameraCard);
