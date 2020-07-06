<template>
  <v-layout column justify-center align-center>
    <v-container>
      <div id="grid">
        <template v-for="s in stepsRev">
          <div :key="s + 5100" class="stepsV steps">{{ s }}%</div>
          <template v-for="d in steps">
            <v-img
              :key="s * 100 + d"
              class="img"
              :src="'res/s' + s + '_d' + d + '.jpg'"
              height="3vw"
              width="3vw"
              @click="triggerModal(s, d)"
            ></v-img>
          </template>
        </template>
        <div id="leftbar" class="bar">SUFFERING</div>
        <div id="bottomBar" class="bar">DESERVED</div>
        <template v-for="d in steps">
          <div :key="d + 5200" class="stepsH steps">{{ d }}%</div>
        </template>
        <div id="kyubey">
          <v-img src="res/kyubey.jpg"></v-img>
        </div>
      </div>
    </v-container>
    <v-dialog v-model="modal" max-width="60vw">
      <v-card>
        <v-img
          id="modalImg"
          :src="'res/s' + currentS + '_d' + currendD + '.jpg'"
          height="3vw"
          width="3vw"
        ></v-img>
        <v-card-title> Character Info - {{ currentName }} </v-card-title>
        <v-card-text>
          <p>Suffering: {{ currentS }}%, Deserve: {{ currendD }}%</p>
          <div v-html="currentContent"></div>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" text @click="modal = false">
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
import marked from 'marked'
import dompurify from 'dompurify'
import data from '~/static/data/zh/names.json'

export default {
  data() {
    const steps = [
      5,
      10,
      15,
      20,
      25,
      30,
      35,
      40,
      45,
      50,
      55,
      60,
      65,
      70,
      75,
      80,
      85,
      90,
      95,
      100,
    ]
    return {
      steps,
      stepsRev: [...steps].reverse(),
      modal: false,
      currentModal: '',
      currentS: 0,
      currendD: 0,
      currentName: '',
      currentContent: '',
    }
  },
  methods: {
    triggerModal(s, d) {
      this.currentS = s
      this.currendD = d
      this.modal = true
      const entityId = `s${s}_d${d}`
      this.currentName = data[entityId] || ''
      this.currentContent = 'loading...'
      fetch(`/data/zh/content/${entityId}.md`)
        .then((x) => x.text())
        .then((x) => {
          this.currentContent = marked(dompurify.sanitize(x))
        })
        .catch((x) => {
          this.currentContent = '暂无数据'
        })
    },
  },
}
</script>

<style lang="sass" scoped>
#grid
  display: grid
  grid-template-rows: repeat(20, 3vw) 2vw 3vw
  grid-template-columns: 3vw 2vw repeat(20, 3vw)
  column-gap: 0
  row-gap: 0
  justify-content: center

#leftbar
  grid-row: 1/21
  grid-column: 1
  writing-mode: vertical-lr
  transform: rotate(180deg)
  background: linear-gradient(to top, #5c4cf0, white)

#bottomBar
  grid-row: 22
  grid-column: 3/23
  background: linear-gradient(to left, #5c4cf0, white)

#kyubey
  grid-row: 21/23
  grid-column: 1/3
  vertical-align: center

.steps
  text-align: right
  font-size: 0.9rem

.stepsV
  grid-column: 2

.stepsH
  grid-row: 21

.bar
  color: black
  font-weight: 300
  font-size: 3rem
  text-align: center
  line-height: 100%

.img:hover
  opacity: 0.8
  transition: opacity 0.2s ease-out
  cursor: pointer

#modalImg
  float: right
  margin-top: 4vh
  margin-right: 4vh
  border-radius: 4%
</style>
