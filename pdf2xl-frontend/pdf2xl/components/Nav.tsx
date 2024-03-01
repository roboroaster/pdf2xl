import React from 'react'
import { ModeToggle } from './ModeToggle';
const Nav = () => {
  return (
    <nav className='pt-4 ml-4 mb-4 '>
      <ul className='flex gap-5 items-center jusify-center'>
        <h3 className='text-xl font-mono font-bold '>pdf2xl</h3>
        <li>Home</li>
        <li>About</li>
        <li><ModeToggle /></li>

      </ul>
    </nav>
  )
}

export default Nav
