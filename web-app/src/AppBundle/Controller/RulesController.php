<?php

namespace AppBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Component\HttpFoundation\Request;

class RulesController extends Controller
{
    /**
     * @Route("/rules", name="rules")
     */
    public function logsAction(Request $request)
    {
        // replace this example code with whatever you need
        return $this->render('rules/rules.html.twig', array());
    }

}
