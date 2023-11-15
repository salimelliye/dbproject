/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["core/**/*.html",
  "static/**/*.html",
  "static/dist/output.css",
  "static/dist/*.js",
  "input.css"],
  theme: {
    screens: {
      xs: '380px',
      xsm: '500px',
      sm: '550px',
      s: '650px',
      md: '798px',
      l: '960px',
      lg: '1110px',
      xlg1: '1200px',
      xlg: '1300px',
      xxlg1: '1350px',
      xxlg: '1390px',
      xl: '1536px',
      xxl: '1750px',
      k: '2400px',
    },
    extend: {
      colors: {
        customDarkGreen: '#006e58',
        customLightGreen: '#8FB9B2',
      },
    }
  },
  plugins: [],
}

