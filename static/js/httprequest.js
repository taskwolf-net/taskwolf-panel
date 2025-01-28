class HttpRequest {
  static PREFIX = "https://team.dulno.com/v1";

  constructor(url, method, headers, data) {
    this.url = url;
    this.method = method;
    this.headers = headers;
    this.data = data;
  }

  send(callback) {
    let self = this;
    if (self.headers === undefined) {
      self.headers = [];
    }
    let headers = [...self.headers];
    headers.push({key: "Content-Type", value: "application/json"});
    var token = Cookie.find("panel-token");
    if (token !== null) {
      this.headers.push({key: "Authorization", value: "Bearer " + token});
    }
    var whitelistKey = Cookie.find("dulno-whitelist-key");
    if (whitelistKey !== null) {
      this.headers.push({key: "WHITELIST-KEY", value: whitelistKey});
    }
    const xhr = new XMLHttpRequest();
    xhr.open(self.method, self.url.startsWith("http") ? self.url :
      HttpRequest.PREFIX + self.url);
    for (const entry of headers) {
      xhr.setRequestHeader(entry.key, entry.value);
    }
    xhr.onload = function (e) {
      if (this.status === 417) {
        self.refresh(callback);
        return;
      }
      callback(this.status, xhr.responseText);
    };
    xhr.onerror = function (e) {
      callback(-1, "");
    };
    xhr.send(JSON.stringify(self.data));
  }

  refresh(callback) {
    let self = this;
    let refreshToken = Cookie.find("refresh-token");
    if (refreshToken == null) {
      return;
    }
    let request = new HttpRequest("/verification/refresh/", "POST",
      [], {refreshToken: refreshToken});
    request.send(function (status, responseText) {
      let response = JSON.parse(responseText);
      if (response.success === "true") {
        Cookie.create("token", response.productApiKey, 60 * 60 * 24 * 30);
        Cookie.create("refresh-token", response.refreshToken, 60 * 60 * 24 * 30);
        self.send(callback);
      }
    });
  }
}