#import "@preview/subpar:0.2.2" as _subpar

#let grid(..args) = {
  let figures = args.pos()
  let named = args.named()
  let kind = named.remove("kind", default: "figure")
  let numbering-pattern = named.remove("numbering", default: auto)
  let numbering-sub-ref = named.remove("numbering-sub-ref", default: auto)
  let label = named.at("label", default: none)
  if label == <fig-gm-cooler> {
    named.insert("columns", (7fr, 5fr))
    named.insert("gutter", 8pt)
  }
  context {
    let super-numbering = if numbering-pattern != auto {
      numbering-pattern
    } else {
      (n) => {
        let chapter = counter(heading).get().first()
        [#str(chapter).#numbering("1", n)]
      }
    }
    let sub-ref-numbering = if numbering-sub-ref != auto {
      numbering-sub-ref
    } else {
      (sup, sub) => {
        let chapter = counter(heading).get().first()
        let letter = numbering("(a)", sub)
        [#str(chapter).#numbering("1", sup)#letter]
      }
    }
    _subpar.grid(
      ..figures,
      kind: kind,
      numbering: super-numbering,
      numbering-sub-ref: sub-ref-numbering,
      ..named,
    )
  }
}
