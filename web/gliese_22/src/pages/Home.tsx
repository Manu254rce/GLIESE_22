import { Switch } from '@headlessui/react';
import React, { useState } from 'react'
import useDarkMode from '../hooks/useDarkMode';

function Home() {
  return (
    <div className='bg-slate-400 dark:bg-slate-900 h-screen'>
        <Nav/>
        <Header/>
        <Start/>
    </div>
  )
}

const Nav = () => {
  return (
    <nav className='fixed top-0 left-0 z-10 w-screen
                    backdrop-blur-md backdrop-brightness-125 
                    bg-transparent h-10'>
        <div className='my-1.5 ml-8'>
            <Toggle/>
        </div>
    </nav>
  )
}

export const Toggle = () => {
    const [darkMode, setdarkMode] = useDarkMode();
    const handleMode = () => setdarkMode(!darkMode)

    const [enabled, setenabled] = useState()
    return (
        <Switch.Group>

            <Switch
                checked={enabled}
                onChange={setenabled}
                onClick={handleMode}
                className={`${enabled ? 'bg-slate-900' : 'bg-slate-300'
                    } relative inline-flex h-6 w-11 items-center rounded-full drop-shadow-md transition-all ease-in-out duration-300`}
            >
                <span
                    className={`${enabled ? 'translate-x-6 bg-white drop-shadow-[0_0_2px_#fff]' :
                        'translate-x-1 bg-black drop-shadow-[0_0_2px_#000]'
                        } inline-block h-4 w-4 transform rounded-full transition-all ease-in-out duration-300`}
                />
            </Switch>
        </Switch.Group>
    )
}

function Header() {
  return (
    <section className='h-1/2 bg-gradient-to-r from-indigo-800 to-slate-900'>
        <section className='h-full bg-gradient-to-bl from-transparent to-rose-900'>
            <section className='h-full bg-gradient-to-tl from-blue-900 to-transparent'>
                  <h1 className='text-6xl text-white text-center pt-24
                                font-zrnic'>Gliese 22</h1>
                <h3 className='font-zrnic text-white text-center text-xl mt-3'>
                    Where Data Science meets Astrophysics
                </h3>
            </section>
        </section>
    </section>
  )
}

function Start() {
  return (
    <section className='bg-slate-400 dark:bg-slate-900 
                    drop-shadow-xl h-auto w-3/4 mx-auto my-10'>
        <div className='grid grid-cols-3 gap-3 p-3'>
            <ProjectComponent>ConvNet</ProjectComponent>
            <ProjectComponent>RNNet</ProjectComponent>
            <ProjectComponent>GANNet</ProjectComponent>
        </div>
    </section>
  )
}

const ProjectComponent = (props: {children:React.ReactNode;}) => {
  return (
    <div className='row-span-3 bg-slate-500 dark:bg-slate-800 hover:bg-gradient-to-bl hover:from-rose-600
                 hover:to-indigo-800 mx-auto w-full rounded-md drop-shadow-lg'>
        <div className='h-full hover:bg-gradient-to-br bg-opacity-50
                       rounded-md hover:from-blue-500 hover:to-transparent'>
            <h1 className='text-white font-zrnic text-2xl pt-16 ml-5'>
                {props.children}
            </h1>
            <hr className='w-1/2 ml-5'/>
        </div>
    </div>
  )
}

export default Home