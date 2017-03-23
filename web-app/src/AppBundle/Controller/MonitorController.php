<?php

namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

class MonitorController extends Controller
{

    /**
     * @Route("/monitor", name="monitor")
     */
    public function monitorAction(Request $request)
    {
        // replace this example code with whatever you need
//        return $this->render('monitor/monitor.html.twig', array());

        $response = new Response();
        $result = $this->renderView('monitor/monitor.html.twig', array());
        $response->headers->addCacheControlDirective('no-cache', true);
        $response->headers->addCacheControlDirective('max-age', 0);
        $response->headers->addCacheControlDirective('must-revalidate', true);
        $response->headers->addCacheControlDirective('no-store', true);
        $response->setContent($result);

        return $response;
    }


}
