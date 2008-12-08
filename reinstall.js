
var data = {
  "MOJI stable version": {
    URL: "http://downloads.mozdev.org/moji/moji-0.9.6.xpi",
    IconURL: "http://moji.mozdev.org/moji-icon3.png",
    toString: function() { return this.URL; }
  },

  "Japanese-English word dictionary": {
    URL: "http://downloads.mozdev.org/moji/mojien-0.6.20080306.xpi",
    IconURL: "http://moji.mozdev.org/moji-icon3.png",
    toString: function() { return this.URL; }
  },

  "English Kanji dictionary": {
    URL: "http://downloads.mozdev.org/moji/mojiken-0.5.20071013.xpi",
    IconURL: "http://moji.mozdev.org/moji-icon3.png",
    toString: function() { return this.URL; }
  }
}

function install() {
  var target = {};

  for (var i = 0; i < params.length; i++) {
    if ( document.instForm[params[i]._tag].checked )
      target[params[i]._name] = params[i];
  }
  
  if (!InstallTrigger.updateEnabled())
    return;
  else
    InstallTrigger.install(target);
}
