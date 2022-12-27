(set-env!
 :source-paths #{"src/cljs"}
 :resource-paths #{"html"}

 :dependencies '[[org.clojure/clojure                           "1.8.0"]
                 [org.clojure/clojurescript                     "1.11.60"]
                 [adzerk/boot-cljs                              "2.1.5"]
                 [pandeiro/boot-http                            "0.8.3"]
                 [nrepl/nrepl                                   "1.0.0"]
                 [adzerk/boot-reload                            "0.6.1"]
                 [adzerk/boot-cljs-repl                         "0.4.0"]
                 [cider/piggieback                              "0.5.3"]
                 [weasel                                        "0.7.1"]
                 [com.andrewmcveigh/cljs-time                   "0.5.2"]
                 [compojure                                     "1.5.2"]
                 [org.clojars.magomimmo/shoreleave-remote-ring  "0.3.3"]
                 [org.clojars.magomimmo/shoreleave-remote       "0.3.1"]
                 [boot-environ                                  "1.2.0"]]
 )

(require '[adzerk.boot-cljs      :refer [cljs]]
         '[pandeiro.boot-http    :refer [serve]]
         '[adzerk.boot-reload    :refer [reload]]
         '[adzerk.boot-cljs-repl :refer [cljs-repl start-repl]])

;; define dev task as composition of subtasks
(deftask dev
  "Launch Immediate Feedback Development Environment"
  []
  (comp
   (serve ;:dir "target"
          :handler 'modern-cljs.remotes/app            ;; ring handler
          :resource-root "target"                      ;; root classpath
          :reload true)                                ;; reload ns
   (watch)
   (reload)
   (cljs-repl) ;; before cljs task
   (cljs)
   (target :dir #{"target"})))