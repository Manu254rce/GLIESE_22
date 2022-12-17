/** @type {import('tailwindcss').Config} */

// const plugin = require('tailwindcss/plugin')

module.exports = {
  mode: 'jit',
  content: [
    './src/**/*.{js,jsx,ts,tsx}'
  ],
  darkMode: 'class',
  theme: {
    extend: {

      textShadow:
      {
        default:'0px 2px 8px var(--tw-shadow-color)',
        sm: '0px 0px 2px var(--tw-shadow-color)',
        md: '0px 0px 8px var(--tw-shadow-color)',
        lg: '0px 0px 16px var(--tw-shadow-color)',
      },

      fontFamily:
      {
        'adventpro': '"Advent Pro"',
        'zrnic': 'Zrnic',
        'audiowide': 'Audiowide',
        'novaflat' : '"Nova Flat"',
      }
    },
  },
  // plugins: [
  //   require("tailwindcss-scrollbar"),
  //   require("tailwindcss-textshadow"),

  //   plugin(function ({matchUtilities, theme})
  //   {
  //     matchUtilities(
  //       {
  //         'text-shadow' : (value) => ({
  //           textShadow : value,
  //         }),
  //       },
  //       { values: theme('textShadow')}
  //     )
  //   }),
  // ],
}