/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      boxShadow:{
        'md': '5px 5px 15px 0 rgb(215, 215, 215)',
        'sm': '0px 2px 6px 0 rgb(215, 215, 215)',
        'ssm': '0px 1px 4px 0 rgb(215, 215, 215)',
        'blackmd': 'box-shadow: 0 1px 3px -2px black'
      },
      flex:{
        'bigger': '2 1 0'
      },
      backgroundColor:{
        'backdrop' : 'rgba(0, 0, 0, 0.75)'
      }
    },
  },
  plugins: [],
}

