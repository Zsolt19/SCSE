import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import REact from 'react';
import HomePage from '../../pages/HomePage.jsx';
import SecondPage from '../../pages/SecondPage.jsx'
// import About from '../../pages/About.jsx';
// import ContactUs from '../../pages/ContactUs.jsx';
import NavBar from './NavBar.jsx';

const MyRoutes=() =>{
  return (
    <>
     <Router>
        <NavBar />
         <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="//secondpage" element={<SecondPage/>}/>
            {/* <Route path="/ContactUs" element={<ContactUs/>}/> */}
         </Routes>
     </Router>
    </>
  );
}  

export default MyRoutes;