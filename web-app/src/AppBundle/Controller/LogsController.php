<?php

namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Request;

class LogsController extends Controller
{
    /**
     * @Route("/logs", name="logs")
     */
    public function logsAction(Request $request)
    {
        // replace this example code with whatever you need
        return $this->render('logs/logs.html.twig', array());
    }

}
