
import { Button, CssBaseline, Typography} from '@mui/material'
import React from 'react'
import { Search } from '../Components/Search'
import { Box } from '@mui/system'
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import cities from '../cities'
import csv from '../csvjson.json'
import Ingredients from '../Components/Ingredients';

export const Home = () => {
    const [show, setShow] = React.useState(false);
    const handleClick = () => {
        setShow(true);
    }



  return (
    
    <div >
   <CssBaseline />
  
   <Typography variant="h3" component="div" gutterBottom className='center' color= "white" >
                Nutri-Fix
            </Typography>
       <Box
        display="flex"
        flexDirection="row"
        gap="1rem"
        alignItems="center"
        justifyContent="center"
        p={20}
    


        bgcolor="background.dark"
        >
            
   
      
        <Search name="Location" options={cities}/>
        <Search name="Disease" options={csv}/>
        <Button variant="Text" endIcon={<ArrowForwardIcon/>} onClick={handleClick} style={{color:"white"}}></Button>
      
  </Box>

<div className='Ingredients' style={{display: show ? 'block' : 'none'}}>
<Ingredients/>
<br/>
<Button variant="Text" endIcon={<ArrowForwardIcon/>}  style={{color:"white"}} href= "/suggestions">Search</Button>
</div>
  

   

  


 

   

    
    </div>
  )
}
