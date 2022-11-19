;; create the main project namespace
(ns weather-e-ink-display.core
  (:require [cljs-time.core :as time]
            [cljs-time.format :as fmt]))

;; enable cljs to print to the JS console of the browser
(enable-console-print!)
(println "Hello, World!")

(-> js/document
     (.getElementById "date")
     (.-innerHTML)
     (set! 
      (fmt/unparse 
       (fmt/formatter "EEEE, MMM dd") 
       (time/to-default-time-zone (js/Date.)))))
