<?php

namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Request;

class MonitorController extends Controller
{

    /**
     * @Route("/monitor", name="monitor")
     */
    public function monitorAction(Request $request)
    {
        // replace this example code with whatever you need
        return $this->render('monitor/monitor.html.twig', array());
    }


}
