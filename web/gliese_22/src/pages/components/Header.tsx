import React from 'react'

const Header = () => {
  return (
    <div className='bg-gradient-to-r 
                    from-indigo-900 to-rose-700
                    h-1/2'>
    <div className='h-full bg-gradient-to-bl 
                    from-slate-900 to-transparent 
                    bg-opacity-40'>
    <div className='h-full bg-gradient-to-r from-transparent
                    to-violet-900'>
        <h1 className='pt-24 text-center text-white font-zrnic
                       text-7xl'>GLIESE_22</h1>
        <h3 className='text-center mt-5 text-white text-xl'>Where Data Science meets Astrophysics</h3>
    </div>
    </div>
    </div>
  )
}

export default Header