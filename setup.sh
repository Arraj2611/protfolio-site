mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#40E0D0'\n\
backgroundColor = '#000000'\n\
secondaryBackgroundColor = '#110c11'\n\
textColor = '#fff'\n\
" > ~/.streamlit/config.toml