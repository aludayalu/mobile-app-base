import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { NextUIProvider } from '@nextui-org/react'
import { createTheme } from "@nextui-org/react"
import { CssBaseline } from '@nextui-org/react';
const theme = createTheme({
	type: "dark", // it could be "light" or "dark"
	theme: {
		colors: {
			// brand colors
			background: '#000',
			text: '#fff',
			// you can also create your own color
			myDarkColor: '#ff4ecd'
			// ...  more colors
		  },
		  space: {},
		  fonts: {}
	}
  })

const container = document.getElementById('root');
const root = createRoot(container!);
root.render(
  <React.StrictMode>
    {CssBaseline.flush()}
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap" rel="stylesheet"/>
    <NextUIProvider theme={theme}>
      <App />
    </NextUIProvider>
  </React.StrictMode>
);