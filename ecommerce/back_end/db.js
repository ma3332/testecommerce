const mongoose = require('mongoose');

mongoose.connect(
  'mongodb://localhost:27017/test',
  {useNewUrlParser: true, useUnifiedTopology: true},
).then(()=>{
    console.log('Connection ok');
}).catch((error) => {
    console.log('Connection fail', error);
});

const paymentSchema = new mongoose.Schema({
  id: String,
  itemId: String,
  paid: Boolean
});
const Payment = mongoose.model('Payment', paymentSchema);

module.exports = {
  Payment
};