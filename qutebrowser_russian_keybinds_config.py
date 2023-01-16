config.load_autoconfig()

# Russian key binds

# mode="caret"
config.bind("П", "move-to-end-of-document", mode="caret")
config.bind("Р", "scroll left", mode="caret")
config.bind("О", "scroll down", mode="caret")
config.bind("Л", "scroll up", mode="caret")
config.bind("Д", "scroll right", mode="caret")
config.bind("М", "selection-toggle --line", mode="caret")
config.bind("Н", "yank selection -s", mode="caret")
config.bind("х", "move-to-start-of-prev-block", mode="caret")
config.bind("ъ", "move-to-start-of-next-block", mode="caret")
config.bind("и", "move-to-prev-word", mode="caret")
config.bind("с", "mode-enter normal", mode="caret")
config.bind("е", "move-to-end-of-word", mode="caret")
config.bind("пп", "move-to-start-of-document", mode="caret")
config.bind("р", "move-to-prev-char", mode="caret")
config.bind("о", "move-to-next-line", mode="caret")
config.bind("л", "move-to-prev-line", mode="caret")
config.bind("д", "move-to-next-char", mode="caret")
config.bind("щ", "selection-reverse", mode="caret")
config.bind("м", "selection-toggle", mode="caret")
config.bind("ц", "move-to-next-word", mode="caret")
config.bind("н", "yank selection", mode="caret")

# mode="command"
config.bind("<Alt-И>", "rl-backward-word", mode="command")
config.bind("<Alt-В>", "rl-kill-word", mode="command")
config.bind("<Alt-А>", "rl-forward-word", mode="command")
config.bind("<Ctrl-,>", "rl-delete-char", mode="command")
config.bind("<Ctrl-Ф>", "rl-beginning-of-line", mode="command")
config.bind("<Ctrl-И>", "rl-backward-char", mode="command")
config.bind("<Ctrl-С>", "completion-item-yank", mode="command")
config.bind("<Ctrl-В>", "completion-item-del", mode="command")
config.bind("<Ctrl-У>", "rl-end-of-line", mode="command")
config.bind("<Ctrl-А>", "rl-forward-char", mode="command")
config.bind("<Ctrl-Р>", "rl-backward-delete-char", mode="command")
config.bind("<Ctrl-Л>", "rl-kill-line", mode="command")
config.bind("<Ctrl-Т>", "command-history-next", mode="command")
config.bind("<Ctrl-З>", "command-history-prev", mode="command")
config.bind("<Ctrl-Shift-С>", "completion-item-yank --sel", mode="command")
config.bind("<Ctrl-Shift-Ц>", "rl-filename-rubout", mode="command")
config.bind("<Ctrl-Г>", "rl-unix-line-discard", mode="command")
config.bind("<Ctrl-Ц>", 'rl-rubout " "', mode="command")
config.bind("<Ctrl-Н>", "rl-yank", mode="command")

# mode="hint"
config.bind("<Ctrl-И>", "hint all tab-bg", mode="hint")
config.bind("<Ctrl-А>", "hint links", mode="hint")
config.bind("<Ctrl-К>", "hint --rapid links tab-bg", mode="hint")

# mode="insert"
config.bind("<Ctrl-У>", "edit-text", mode="insert")

# mode="normal"
config.bind("э", "mode-enter jump_mark", mode="normal")
config.bind("ю", "repeat-command", mode="normal")
config.bind(".", "set-cmd-text /", mode="normal")
config.bind("Ж", "set-cmd-text :", mode="normal")
config.bind("жШ", "hint images tab", mode="normal")
config.bind("жЩ", "hint links fill :open -t -r {hint-url}", mode="normal")
config.bind("жК", "hint --rapid links window", mode="normal")
config.bind("жН", "hint links yank-primary", mode="normal")
config.bind("жи", "hint all tab-bg", mode="normal")
config.bind("жв", "hint links download", mode="normal")
config.bind("жа", "hint all tab-fg", mode="normal")
config.bind("жр", "hint all hover", mode="normal")
config.bind("жш", "hint images", mode="normal")
config.bind("жщ", "hint links fill :open {hint-url}", mode="normal")
config.bind("жк", "hint --rapid links tab-bg", mode="normal")
config.bind("же", "hint inputs", mode="normal")
config.bind("жн", "hint links yank", mode="normal")
config.bind("<Alt-ь>", "tab-mute", mode="normal")
config.bind("<Ctrl-Ф>", "navigate increment", mode="normal")
config.bind("<Ctrl-Alt-з>", "print", mode="normal")
config.bind("<Ctrl-И>", "scroll-page 0 -1", mode="normal")
config.bind("<Ctrl-В>", "scroll-page 0 0.5", mode="normal")
config.bind("<Ctrl-А>", "scroll-page 0 1", mode="normal")
config.bind("<Ctrl-Т>", "open -w", mode="normal")
config.bind("<Ctrl-Й>", "quit", mode="normal")
config.bind("<Ctrl-Shift-Т>", "open -p", mode="normal")
config.bind("<Ctrl-Shift-Е>", "undo", mode="normal")
config.bind("<Ctrl-Shift-Ц>", "close", mode="normal")
config.bind("<Ctrl-Е>", "open -t", mode="normal")
config.bind("<Ctrl-Г>", "scroll-page 0 -0.5", mode="normal")
config.bind("<Ctrl-М>", "mode-enter passthrough", mode="normal")
config.bind("<Ctrl-Ц>", "tab-close", mode="normal")
config.bind("<Ctrl-Ч>", "navigate decrement", mode="normal")
config.bind("<Ctrl-:>", "tab-focus last", mode="normal")
config.bind("<Ctrl-р>", "home", mode="normal")
config.bind("<Ctrl-з>", "tab-pin", mode="normal")
config.bind("<Ctrl-ы>", "stop", mode="normal")
config.bind(",", "set-cmd-text ?", mode="normal")
config.bind('"', "macro-run", mode="normal")
config.bind("И", "set-cmd-text -s :quickmark-load -t", mode="normal")
config.bind("В", "tab-close -o", mode="normal")
config.bind("А", "hint all tab", mode="normal")
config.bind("П", "scroll-to-perc", mode="normal")
config.bind("Р", "back", mode="normal")
config.bind("О", "tab-next", mode="normal")
config.bind("Л", "tab-prev", mode="normal")
config.bind("Д", "forward", mode="normal")
config.bind("Ь", "bookmark-add", mode="normal")
config.bind("Т", "search-prev", mode="normal")
config.bind("Щ", "set-cmd-text -s :open -t", mode="normal")
config.bind("ЗЗ", "open -t -- {primary}", mode="normal")
config.bind("Зз", "open -t -- {clipboard}", mode="normal")
config.bind("К", "reload -f", mode="normal")
config.bind("Ыи", "bookmark-list --jump", mode="normal")
config.bind("Ыр", "history", mode="normal")
config.bind("Ый", "bookmark-list", mode="normal")
config.bind("Ыы", "set", mode="normal")
config.bind("Е", "set-cmd-text -sr :tab-focus", mode="normal")
config.bind("Г", "undo -w", mode="normal")
config.bind("М", "mode-enter caret ;; selection-toggle --line", mode="normal")
config.bind("ЯЙ", "quit", mode="normal")
config.bind("ЯЯ", "quit --save", mode="normal")
config.bind("хх", "navigate prev", mode="normal")
config.bind("ъъ", "navigate next", mode="normal")
config.bind("ё", "mode-enter set_mark", mode="normal")
config.bind("фв", "download-cancel", mode="normal")
config.bind("и", "set-cmd-text -s :quickmark-load", mode="normal")
config.bind("св", "download-clear", mode="normal")
config.bind("сщ", "tab-only", mode="normal")
config.bind("в", "tab-close", mode="normal")
config.bind("а", "hint", mode="normal")
config.bind("п;", "tab-focus -1", mode="normal")
config.bind("п0", "tab-focus 1", mode="normal")
config.bind("пИ", "set-cmd-text -s :bookmark-load -t", mode="normal")
config.bind("пС", "tab-clone", mode="normal")
config.bind("пВ", "tab-give", mode="normal")
config.bind("пО", "tab-move +", mode="normal")
config.bind("пЛ", "tab-move -", mode="normal")
config.bind("пЩ", "set-cmd-text :open -t -r {url:pretty}", mode="normal")
config.bind("пГ", "navigate up -t", mode="normal")
config.bind("п:", "tab-focus 1", mode="normal")
config.bind("пф", "open -t", mode="normal")
config.bind("пи", "set-cmd-text -s :bookmark-load", mode="normal")
config.bind("пв", "download", mode="normal")
config.bind("па", "view-source", mode="normal")
config.bind("пп", "scroll-to-perc 0", mode="normal")
config.bind("пш", "hint inputs --first", mode="normal")
config.bind("пь", "tab-move", mode="normal")
config.bind("пщ", "set-cmd-text :open {url:pretty}", mode="normal")
config.bind("пе", "set-cmd-text -s :tab-select", mode="normal")
config.bind("пг", "navigate up", mode="normal")
config.bind("р", "scroll left", mode="normal")
config.bind("ш", "mode-enter insert", mode="normal")
config.bind("о", "scroll down", mode="normal")
config.bind("л", "scroll up", mode="normal")
config.bind("д", "scroll right", mode="normal")
config.bind("ь", "quickmark-save", mode="normal")
config.bind("т", "search-next", mode="normal")
config.bind("щ", "set-cmd-text -s :open", mode="normal")
config.bind("зЗ", "open -- {primary}", mode="normal")
config.bind("зз", "open -- {clipboard}", mode="normal")
config.bind("й", "macro-record", mode="normal")
config.bind("к", "reload", mode="normal")
config.bind("ыа", "save", mode="normal")
config.bind("ыл", "set-cmd-text -s :bind", mode="normal")
config.bind("ыд", "set-cmd-text -s :set -t", mode="normal")
config.bind("ыы", "set-cmd-text -s :set", mode="normal")
config.bind(
    "еСР",
    "config-cycle -p -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
    mode="normal",
)
config.bind(
    "еСр",
    "config-cycle -p -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
    mode="normal",
)
config.bind(
    "еСг",
    "config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload",
    mode="normal",
)
config.bind(
    "еШР",
    "config-cycle -p -u *://*.{url:host}/* content.images ;; reload",
    mode="normal",
)
config.bind(
    "еШр", "config-cycle -p -u *://{url:host}/* content.images ;; reload", mode="normal"
)
config.bind("еШг", "config-cycle -p -u {url} content.images ;; reload", mode="normal")
config.bind(
    "еЗР",
    "config-cycle -p -u *://*.{url:host}/* content.plugins ;; reload",
    mode="normal",
)
config.bind(
    "еЗр",
    "config-cycle -p -u *://{url:host}/* content.plugins ;; reload",
    mode="normal",
)
config.bind("еЗг", "config-cycle -p -u {url} content.plugins ;; reload", mode="normal")
config.bind(
    "еЫР",
    "config-cycle -p -u *://*.{url:host}/* content.javascript.enabled ;; reload",
    mode="normal",
)
config.bind(
    "еЫр",
    "config-cycle -p -u *://{url:host}/* content.javascript.enabled ;; reload",
    mode="normal",
)
config.bind(
    "еЫг",
    "config-cycle -p -u {url} content.javascript.enabled ;; reload",
    mode="normal",
)
config.bind(
    "есР",
    "config-cycle -p -t -u *://*.{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
    mode="normal",
)
config.bind(
    "еср",
    "config-cycle -p -t -u *://{url:host}/* content.cookies.accept all no-3rdparty never ;; reload",
    mode="normal",
)
config.bind(
    "есг",
    "config-cycle -p -t -u {url} content.cookies.accept all no-3rdparty never ;; reload",
    mode="normal",
)
config.bind("ер", "back -t", mode="normal")
config.bind(
    "ешР",
    "config-cycle -p -t -u *://*.{url:host}/* content.images ;; reload",
    mode="normal",
)
config.bind(
    "ешр",
    "config-cycle -p -t -u *://{url:host}/* content.images ;; reload",
    mode="normal",
)
config.bind(
    "ешг", "config-cycle -p -t -u {url} content.images ;; reload", mode="normal"
)
config.bind("ед", "forward -t", mode="normal")
config.bind(
    "езР",
    "config-cycle -p -t -u *://*.{url:host}/* content.plugins ;; reload",
    mode="normal",
)
config.bind(
    "езр",
    "config-cycle -p -t -u *://{url:host}/* content.plugins ;; reload",
    mode="normal",
)
config.bind(
    "езг", "config-cycle -p -t -u {url} content.plugins ;; reload", mode="normal"
)
config.bind(
    "еыР",
    "config-cycle -p -t -u *://*.{url:host}/* content.javascript.enabled ;; reload",
    mode="normal",
)
config.bind(
    "еыр",
    "config-cycle -p -t -u *://{url:host}/* content.javascript.enabled ;; reload",
    mode="normal",
)
config.bind(
    "еыг",
    "config-cycle -p -t -u {url} content.javascript.enabled ;; reload",
    mode="normal",
)
config.bind("г", "undo", mode="normal")
config.bind("м", "mode-enter caret", mode="normal")
config.bind("цИ", "set-cmd-text -s :bookmark-load -w", mode="normal")
config.bind("цШа", "devtools-focus", mode="normal")
config.bind("цШр", "devtools left", mode="normal")
config.bind("цШо", "devtools bottom", mode="normal")
config.bind("цШл", "devtools top", mode="normal")
config.bind("цШд", "devtools right", mode="normal")
config.bind("цШц", "devtools window", mode="normal")
config.bind("цЩ", "set-cmd-text :open -w {url:pretty}", mode="normal")
config.bind("цЗ", "open -w -- {primary}", mode="normal")
config.bind("ци", "set-cmd-text -s :quickmark-load -w", mode="normal")
config.bind("ца", "hint all window", mode="normal")
config.bind("цр", "back -w", mode="normal")
config.bind("цш", "devtools", mode="normal")
config.bind("цд", "forward -w", mode="normal")
config.bind("цщ", "set-cmd-text -s :open -w", mode="normal")
config.bind("цз", "open -w -- {clipboard}", mode="normal")
config.bind("чЩ", "set-cmd-text :open -b -r {url:pretty}", mode="normal")
config.bind("чщ", "set-cmd-text -s :open -b", mode="normal")
config.bind("нВ", "yank domain -s", mode="normal")
config.bind("нЬ", "yank inline [{title}]({url}) -s", mode="normal")
config.bind("нЗ", "yank pretty-url -s", mode="normal")
config.bind("нЕ", "yank title -s", mode="normal")
config.bind("нН", "yank -s", mode="normal")
config.bind("нв", "yank domain", mode="normal")
config.bind("нь", "yank inline [{title}]({url})", mode="normal")
config.bind("нз", "yank pretty-url", mode="normal")
config.bind("не", "yank title", mode="normal")
config.bind("нн", "yank", mode="normal")
config.bind("ХХ", "navigate prev -t", mode="normal")
config.bind("ЪЪ", "navigate next -t", mode="normal")

# mode="prompt"
config.bind("<Alt-И>", "rl-backward-word"               , mode="prompt")
config.bind("<Alt-В>", "rl-kill-word"                   , mode="prompt")
config.bind("<Alt-А>", "rl-forward-word"                , mode="prompt")
config.bind("<Alt-Shift-Н>", "prompt-yank --sel"        , mode="prompt")
config.bind("<Alt-Н>", "prompt-yank"                    , mode="prompt")
config.bind("<Ctrl-,>", "rl-delete-char"                , mode="prompt")
config.bind("<Ctrl-Ф>", "rl-beginning-of-line"          , mode="prompt")
config.bind("<Ctrl-И>", "rl-backward-char"              , mode="prompt")
config.bind("<Ctrl-У>", "rl-end-of-line"                , mode="prompt")
config.bind("<Ctrl-А>", "rl-forward-char"               , mode="prompt")
config.bind("<Ctrl-Р>", "rl-backward-delete-char"       , mode="prompt")
config.bind("<Ctrl-Л>", "rl-kill-line"                  , mode="prompt")
config.bind("<Ctrl-З>", "prompt-open-download --pdfjs"  , mode="prompt")
config.bind("<Ctrl-Shift-Ц>", "rl-filename-rubout"      , mode="prompt")
config.bind("<Ctrl-Г>", "rl-unix-line-discard"          , mode="prompt")
config.bind("<Ctrl-Ц>", 'rl-rubout " "'                 , mode="prompt")
config.bind("<Ctrl-Ч>", "prompt-open-download"          , mode="prompt")
config.bind("<Ctrl-Н>", "rl-yank"                       , mode="prompt")

# mode="yesno"
config.bind("<Alt-Shift-Н>", "prompt-yank --sel"  , mode="yesno")
config.bind("<Alt-Н>", "prompt-yank"              , mode="yesno")
config.bind("Т", "prompt-accept --save no"        , mode="yesno")
config.bind("Н", "prompt-accept --save yes"       , mode="yesno")
config.bind("т", "prompt-accept no"               , mode="yesno")
config.bind("н", "prompt-accept yes"              , mode="yesno")